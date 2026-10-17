"""Validate new catalog assets by reopening each .blend and reimporting each GLB.

Run: blender -b -t 2 --python scripts/validate_catalog.py
"""
import bpy
import json
import math
import struct
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
records=json.loads((ROOT/'data/24_minerios.json').read_text())+json.loads((ROOT/'data/28_picaretas.json').read_text())
records=[r for r in records if r['id'] not in {'O03','O04'}]
results=[]
errors=[]
for rec in records:
    asset_id=rec['id']
    stem=next((p.stem for p in (ROOT/'models').glob(f'BH_*_{asset_id}_*_V01.blend')),None)
    try:
        assert stem, 'blend missing'
        model=ROOT/'models'/f'{stem}.blend'
        glb=ROOT/'exports'/f'{stem}.glb'
        bpy.ops.wm.open_mainfile(filepath=str(model))
        data={}
        for cname in ['01 MASTER | detailed','02 GAME | optimized']:
            c=bpy.data.collections[cname]
            objs=[o for o in c.objects if o.type=='MESH']
            assert objs, cname+' empty'
            tri=sum(len(p.vertices)-2 for o in objs for p in o.data.polygons)
            assert all(abs(o.matrix_world[i][j]-(1 if i==j else 0))<1e-5 for o in objs for i in range(4) for j in range(4)), cname+' unapplied transform'
            v=[o.matrix_world@vert.co for o in objs for vert in o.data.vertices]
            dims=[round(max(x[i] for x in v)-min(x[i] for x in v),3) for i in range(3)]
            data[cname]={'meshes':len(objs),'triangles':tri,'dimensions':dims}
        assert data['02 GAME | optimized']['triangles']<5000, 'game triangle budget'
        assert glb.is_file() and glb.stat().st_size>1000, 'GLB missing or empty'
        before=set(bpy.data.objects)
        bpy.ops.import_scene.gltf(filepath=str(glb))
        imported=[o for o in bpy.data.objects if o not in before and o.type=='MESH']
        glb_tri=sum(len(p.vertices)-2 for o in imported for p in o.data.polygons)
        assert glb_tri==data['02 GAME | optimized']['triangles'], 'GLB triangle mismatch'
        assert len(imported)==data['02 GAME | optimized']['meshes'], 'GLB mesh count mismatch'
        pngs=[]
        for view in ['Front','Iso','Back']:
            p=ROOT/'renders'/f'{stem}_{view}.png'
            assert p.is_file(), view+' missing'
            with p.open('rb') as f:h=f.read(24)
            assert h[:8]==b'\x89PNG\r\n\x1a\n' and struct.unpack('>II',h[16:24])==(1024,1024), view+' invalid PNG'
            pngs.append(p.stat().st_size)
        results.append({'id':asset_id,'name':rec['name'],'stem':stem,'master':data['01 MASTER | detailed'],'game':data['02 GAME | optimized'],'glb_triangles':glb_tri,'render_bytes':pngs})
        print('VALID_OK',asset_id,glb_tri,flush=True)
    except Exception as exc:
        errors.append({'id':asset_id,'error':str(exc)})
        print('VALID_FAIL',asset_id,str(exc),flush=True)
out={'validated':len(results),'expected':len(records),'errors':errors,'assets':results}
(ROOT/'docs/Catalog_Validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
if errors:raise SystemExit('Catalog validation failed')
print('CATALOG_VALIDATION_OK',len(results),flush=True)
