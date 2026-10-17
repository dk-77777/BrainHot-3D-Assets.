"""Reopen all V02 assets, verify topology/transforms/dimensions and GLB round trips."""
import bpy,bmesh,json,hashlib,struct,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from art_v02_common import stats
ROOT=Path(__file__).resolve().parents[1]
IDS=[f'O{i:02}' for i in range(1,25)]+['P01','P05','P06','P12','P16']
if '--picks' in sys.argv:IDS=[i for i in IDS if i.startswith('P')]
if '--id' in sys.argv:IDS=[sys.argv[sys.argv.index('--id')+1]]
results=[];errors=[]
for aid in IDS:
    try:
        p=next((ROOT/'models').glob(f'BH_*_{aid}_*_V02.blend'))
        bpy.ops.wm.open_mainfile(filepath=str(p))
        master=next(c for c in bpy.data.collections if c.name.startswith('01 MASTER'))
        game=next(c for c in bpy.data.collections if c.name.startswith('02 GAME'))
        a,b=stats(master),stats(game)
        assert b['triangles']>0 and b['triangles']<6500,'unexpected geometry count'
        topology=[]
        for o in list(master.objects)+list(game.objects):
            assert all(abs(o.matrix_world[i][j]-(1 if i==j else 0))<1e-5 for i in range(4) for j in range(4)),o.name+' transform'
            assert all(__import__('math').isfinite(float(x)) for v in o.data.vertices for x in v.co),'non-finite vertex'
            bm=bmesh.new();bm.from_mesh(o.data)
            boundary=sum(not e.is_manifold for e in bm.edges)
            degenerates=sum(f.calc_area()<1e-10 for f in bm.faces)
            bm.free()
            if boundary or degenerates:topology.append({'mesh':o.name,'nonmanifold_edges':boundary,'zero_area_faces':degenerates})
        assert not topology,'topology issues '+str(topology)
        data={'id':aid,'stem':p.stem,'master':a,'game':b,'topology_issues':topology}
        if aid.startswith('O'):
            ref=next(c for c in bpy.data.collections if c.name=='00 REFERENCE_GAME_V01')
            old=stats(ref)
            ratios=[round(b['dimensions'][i]/old['dimensions'][i],4) for i in range(3)]
            assert all(1.099<r<1.251 for r in ratios),'scale beyond requested range '+str(ratios)
            data['scale_ratios_xyz']=ratios
        else:
            assert '03 AURA_PREVIEW | not gameplay' in bpy.data.collections,'missing aura'
            data['aura_meshes']=len(bpy.data.collections['03 AURA_PREVIEW | not gameplay'].objects)
        before=set(bpy.data.objects)
        bpy.ops.import_scene.gltf(filepath=str(ROOT/'exports'/f'{p.stem}.glb'))
        imp=[o for o in bpy.data.objects if o not in before and o.type=='MESH']
        tri=sum(len(f.vertices)-2 for o in imp for f in o.data.polygons)
        assert tri==b['triangles'],f'GLB triangle mismatch {tri} vs {b["triangles"]}'
        assert len(imp)==b['meshes'],'GLB included extra objects or missed model meshes'
        bpy.context.view_layer.update()
        iv=[o.matrix_world@v.co for o in imp for v in o.data.vertices]
        idims=[round(max(v[i] for v in iv)-min(v[i] for v in iv),4) for i in range(3)]
        assert all(abs(idims[i]-b['dimensions'][i])<.002 for i in range(3)),'GLB dimensions mismatch'
        assert all(o.matrix_world.translation.length<1e-4 for o in imp),'GLB pivot translation mismatch'
        data['glb_triangles']=tri;data['glb_dimensions']=idims
        views=['Front','Iso','Back','Before_After'] if aid.startswith('O') else ['Front','Iso','Dark']
        if '--mesh-only' in sys.argv:views=[]
        for view in views:
            img=ROOT/'renders'/f'{p.stem}_{view}.png'
            with img.open('rb') as f:h=f.read(24)
            dims=struct.unpack('>II',h[16:24]);expected=(1536,1024) if view=='Before_After' else (1024,1024)
            assert h[:8]==b'\x89PNG\r\n\x1a\n' and dims==expected,'render size '+view
        results.append(data);print('V02_VALID_OK',aid,tri,flush=True)
    except Exception as e:
        errors.append({'id':aid,'error':str(e)});print('V02_VALID_FAIL',aid,str(e),flush=True)
out={'expected':len(IDS),'passed':len(results),'errors':errors,'assets':results}
(ROOT/'docs'/('Art_V02_Mesh_Preflight.json' if '--mesh-only' in sys.argv else 'Pickaxe_V02_Validation.json' if '--picks' in sys.argv else 'Single_V02_Validation.json' if '--id' in sys.argv else 'Art_V02_Validation.json')).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('V02_VALIDATION',len(results),len(errors),flush=True)
if errors:raise SystemExit(1)
