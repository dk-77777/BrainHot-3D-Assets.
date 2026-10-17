"""Refine existing V01 ores; preserve original files and source collections.
Run: blender -b -t 4 --python scripts/refine_ores_v02.py -- --id O03 / --all
"""
import sys,math,json,random
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from art_v02_common import *
from build_catalog import ORES,PALETTES,slug,spire
PALETTES.update({'O03':((.05,.025,.08),(.40,.09,.72)),'O04':((.07,.04,.025),(.88,.31,.035))})
CRYSTAL_IDS={'O02','O03','O04','O06','O08','O09','O10','O12','O14','O16','O17','O20','O22','O24'}


def source_path(oid):
    if oid=='O03':return ROOT/'models/Twilight_Crystal_Ore.blend'
    if oid=='O04':return ROOT/'models/Spirit_Amber_Ore.blend'
    return next((ROOT/'models').glob(f'BH_ORE_{oid}_*_V01.blend'))


def copy_col(src,name):
    dst=collection(name)
    for o in src.objects:
        if o.type!='MESH':continue
        d=o.copy();d.data=o.data.copy();dst.objects.link(d);d.hide_set(False);d.hide_render=False
    return dst


def bbox(o):
    verts=[o.matrix_world@v.co for v in o.data.vertices]
    lo=Vector(tuple(min(v[i] for v in verts) for i in range(3)))
    hi=Vector(tuple(max(v[i] for v in verts) for i in range(3)))
    return lo,hi


def shade(o,mats,seed):
    o.data.materials.clear()
    for m in mats:o.data.materials.append(m)
    for p in o.data.polygons:
        if len(mats)==1:p.material_index=0
        else:
            score=(p.normal.x*.7-p.normal.y*.4+p.normal.z*.35+1.45)/2.9
            p.material_index=min(len(mats)-1,max(0,int(score*len(mats))))


def surface(rocks,x,y,top):
    best=None
    for o in rocks:
        hit,p,n,f=o.ray_cast(Vector((x,y,top+3)),Vector((0,0,-1)))
        if hit and (best is None or p.z>best.z):best=p
    return best


def repair_surface(o):
    bm=bmesh.new();bm.from_mesh(o.data)
    bmesh.ops.remove_doubles(bm,verts=list(bm.verts),dist=1e-7)
    bmesh.ops.dissolve_degenerate(bm,edges=list(bm.edges),dist=1e-7)
    boundary=[e for e in bm.edges if e.is_boundary]
    if boundary:bmesh.ops.holes_fill(bm,edges=boundary,sides=0)
    bmesh.ops.recalc_face_normals(bm,faces=list(bm.faces))
    bm.to_mesh(o.data);bm.free();o.data.update()


def refine(col,oid,low):
    index=int(oid[1:]);rng=random.Random(index*41);primary,accent=PALETTES[oid]
    stone=[material(f'{oid} V02 | basalt shadow',(.028+.007*(index%3),.032,.045),.08,.88),
           material(f'{oid} V02 | stone mid',(.066,.070,.081),.10,.79),
           material(f'{oid} V02 | rock worn plane',(.11,.12,.14),.12,.68)]
    if oid=='O07':
        stone=[material('O07 V02 | lunar shadow',(.22,.25,.29),.05,.9),material('O07 V02 | lunar mid',(.42,.46,.51),.04,.78),material('O07 V02 | lunar edge',(.60,.65,.69),.05,.68)]
    crystal=[material(f'{oid} V02 | crystal deep',tuple(x*.36 for x in accent),.10,.28),
             material(f'{oid} V02 | crystal body',tuple(x*.68 for x in accent),.13,.22),
             material(f'{oid} V02 | crystal clear face',accent,.12,.16),
             material(f'{oid} V02 | crystal tip',tuple(min(.93,x*.8+.18) for x in accent),.08,.13)]
    line_mat=material(f'{oid} V02 | mineral inlay',accent,.03,.45,.25+index*.017)
    crack_mat=material(f'{oid} V02 | deep rock seam',(.012,.014,.022),0,.95)
    captive=material(f'{oid} V02 | captive firefly light',(1,.67,.11),.02,.28,1.1) if oid=='O04' else line_mat
    rocks=[];crystals=[]
    all_before=stats(col)
    for o in list(col.objects):
        n=o.name.lower()
        if any(k in n for k in ['blue mist fissure','luminous fissure','molten seam','amber vein','deep inscription']) or (oid=='O07' and 'crater rim' in n):
            bpy.data.objects.remove(o,do_unlink=True);continue
        repair_surface(o)
        rockish=any(k in n for k in ['bedrock','shoulder','stone','slate','fragment','chip','basalt','main fractured','loose','fractured rim'])
        # Keep the void fragments, nullstone and obsidian blades distinct from the bedrock.
        if any(k in n for k in ['anomaly','monolith','ritual','axis','halo','eclipse disk']):rockish=False
        if rockish:
            rocks.append(o);shade(o,stone,index)
            lo,hi=bbox(o);ctr=(lo+hi)*.5
            for v in o.data.vertices:
                if v.co.z>lo.z+(hi.z-lo.z)*.45:
                    v.co.z=lo.z+(v.co.z-lo.z)*1.08
        elif 'captive light' in n:shade(o,[captive],index)
        elif any(k in n for k in ['fissure','seam','incision','inscription','rune line','vein','arcane heart']):shade(o,[line_mat],index)
        elif any(k in n for k in ['root','bronze','seal','cage']):
            continue
        else:
            shade(o,crystal if oid in CRYSTAL_IDS else [stone[0],stone[1],crystal[0]],index)
            if any(k in n for k in ['shard','amethyst','prism','resin','sapphire','quartz','heart']):
                crystals.append(o)
                lo,hi=bbox(o);ctr=(lo+hi)*.5;height=max(.01,hi.z-lo.z)
                for v in o.data.vertices:
                    t=(v.co.z-lo.z)/height
                    if t>.83 and 'resin' not in n:
                        f=1-.30*(t-.83)/.17
                        v.co.x=ctr.x+(v.co.x-ctr.x)*f;v.co.y=ctr.y+(v.co.y-ctr.y)*f
        o.data.update()
        if not any(k in n for k in ['fissure','vein','seam','rune','inscription','root','crater','halo']) and len(o.data.polygons)<200:
            bpy.context.view_layer.objects.active=o
            mod=o.modifiers.new('V02 fine crafted bevel','BEVEL');mod.width=.006 if low else .010;mod.segments=1
            try:bpy.ops.object.modifier_apply(modifier=mod.name)
            except RuntimeError:o.modifiers.remove(mod)
    if oid=='O07':
        dome=next(o for o in col.objects if 'moonstone dome' in o.name.lower())
        bpy.context.view_layer.objects.active=dome
        mod=dome.modifiers.new('Refine original lunar boulder','SUBSURF');mod.levels=1
        bpy.ops.object.modifier_apply(modifier=mod.name)
        for j,(x,y,r) in enumerate([(-.28,-.12,.17),(.20,-.23,.13),(.18,.25,.18),(-.22,.31,.105)]):
            hit,p,n,f=dome.ray_cast(Vector((x,y,3)),Vector((0,0,-1)))
            if hit:
                bpy.ops.mesh.primitive_uv_sphere_add(segments=12,ring_count=8,radius=r,location=(x,y,p.z+r*.28))
                cutter=bpy.context.object;cutter.scale=(1,.95,.80)
                bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
                bpy.context.view_layer.objects.active=dome
                cut=dome.modifiers.new('Shallow sculpted crater','BOOLEAN');cut.operation='DIFFERENCE';cut.solver='EXACT';cut.object=cutter
                bpy.ops.object.modifier_apply(modifier=cut.name)
                bpy.data.objects.remove(cutter,do_unlink=True)
        shade(dome,stone,index);repair_surface(dome)
    # One integrated heart replaces only the three weak core volumes, keeping the original base.
    if oid=='O12':
        for o in list(col.objects):
            if 'heart' in o.name.lower():bpy.data.objects.remove(o,do_unlink=True)
        outline=[(0,.33),(-.53,1.05),(-.64,1.34),(-.48,1.58),(-.23,1.63),(0,1.45),(.23,1.63),(.48,1.58),(.64,1.34),(.53,1.05)]
        n=len(outline);vs=[]
        for y,scale in [(.18,.75),(-.05,1),(-.31,.65)]:
            for x,z in outline:vs.append((x*scale,y,1.12+(z-1.12)*scale))
        fs=[tuple(reversed(range(n)))]
        for j in range(2):
            for i in range(n):fs.append((j*n+i,j*n+(i+1)%n,(j+1)*n+(i+1)%n,(j+1)*n+i))
        fs.append(tuple(2*n+i for i in range(n)))
        h=mesh('O12 | integrated cut heart',vs,fs,crystal,col);shade(h,crystal,index)
        for side in [-1,1]:rock('O12 | integrated basalt cradle',(side*.18,-.13,.43),(.20,.18,.27),stone,col,42+side)
    # Added crystalline shoots remain inside the original envelope; grouping varies by ore.
    if oid in CRYSTAL_IDS and oid not in {'O04','O12','O17'}:
        count=2 if index<7 else 3 if index<19 else 4
        for j in range(count):
            a=index*.47+j*2.34;r=.59+.10*(j%2)
            x=r*math.cos(a);y=r*math.sin(a)
            p=surface(rocks,x,y,all_before['dimensions'][2])
            if p is not None:
                spire(f'{oid} | V02 secondary crystal {j}',(x,y,p.z-.05),.32+.08*(j%3),.09+.02*(j%2),(.09*math.cos(a),.09*math.sin(a)),crystal,col,index*20+j,low,tip=.008)
    elif oid=='O04':
        for j,(x,y) in enumerate([(-.70,-.64),(.70,-.48)]):
            rock('O04 | small amber nodule',(x,y,.47),(.15,.13,.20),crystal,col,index+j)
    # Carved layered ledges enrich existing rock without replacing its layout.
    if rocks:
        for j in range(2 if index<13 else 3):
            a=index*.4+j*2.1;x=.84*math.cos(a);y=.72*math.sin(a)
            p=surface(rocks,x,y,all_before['dimensions'][2])
            if p is not None:rock(f'{oid} | V02 embedded stone ledge',(x,y,max(.14,p.z-.04)),(.20,.14,.09),stone,col,index+j+77)
        # Raycast each fissure point onto the rock to avoid the floating lines seen in V01.
        for j in range(0 if oid=='O07' else 2 if index<13 else 3):
            a=index*.61+j*2.22;pts=[]
            for k in range(7):
                r=.43+k*.065;x=r*math.cos(a)+.027*math.sin(k*2+j);y=r*math.sin(a)+.025*math.cos(k+j)
                p=surface(rocks,x,y,all_before['dimensions'][2])
                if p is not None:pts.append((p.x,p.y,p.z+.003))
            if len(pts)>2:
                line(f'{oid} | V02 recessed surface seam',pts,.009,crack_mat,col)
                if (index>=8 or oid in {'O01','O03'}) and oid not in {'O07','O09'}:line(f'{oid} | V02 mineral vein',[(x,y,z+.001) for x,y,z in pts[1:-1]],.004,line_mat,col)
    if oid=='O05':
        for o in [x for x in col.objects if 'rune slab' in x.name.lower()]:
            lo,hi=bbox(o);x=(lo.x+hi.x)/2;y=lo.y-.004
            line('O05 | forked rune engraving',[(x-.065,y,.90),(x,y,.80),(x+.065,y,.90)],.009,line_mat,col)
    if oid in {'O15','O21'}:
        targets=[o for o in col.objects if ('ritual obsidian blade' in o.name.lower() if oid=='O15' else 'nullstone monolith' in o.name.lower())]
        for j,o in enumerate(targets):
            if oid=='O15':
                a=j*2*math.pi/5
                samples=[((.4+.52*t)*math.cos(a),.42+.95*t) for t in [.30,.46,.62,.75]]
            else:samples=[(-.12+.055*k,.76+.16*k) for k in range(4)]
            pts=[]
            for x,z in samples:
                hit,p,n,f=o.ray_cast(Vector((x,-3,z)),Vector((0,1,0)))
                if hit:pts.append((p.x,p.y-.003,p.z))
            if len(pts)>=3:line(oid+' | surface engraved inscription',pts,.006,line_mat,col)
    if oid=='O24':
        for j in range(5):
            a=j*2*math.pi/5;pts=[]
            for rr,aa in [(1.10,a),(0.76,a-.19),(.76,a+.19)]:pts.append((rr*math.cos(aa),rr*math.sin(aa),.27))
            v=pts+[(x,y,z+.065) for x,y,z in pts]
            mesh('O24 | integrated star ridge',v,[(0,2,1),(3,4,5),(0,1,4,3),(1,2,5,4),(2,0,3,5)],[stone[1]],col)
    # Normalize to the original envelope, then apply the requested uniform scale progression.
    # This avoids hidden size inflation from bevels or secondary elements.
    apply_origins(col)
    verts=[v for o in col.objects if o.type=='MESH' for v in o.data.vertices]
    lo=Vector(tuple(min(v.co[i] for v in verts) for i in range(3)))
    hi=Vector(tuple(max(v.co[i] for v in verts) for i in range(3)))
    factors=[all_before['dimensions'][i]/max(.001,hi[i]-lo[i]) for i in range(3)]
    scale=round(1.12+.11*(index-1)/23,4)
    for v in verts:
        v.co.x*=factors[0]*scale;v.co.y*=factors[1]*scale;v.co.z=(v.co.z-lo.z)*factors[2]*scale
    if low:
        tri=stats(col)['triangles']
        if tri>2850:
            ratio=2850/tri
            for o in col.objects:
                if len(o.data.polygons)>48:
                    bpy.context.view_layer.objects.active=o;mod=o.modifiers.new('V02 mobile reduction','DECIMATE');mod.ratio=ratio
                    bpy.ops.object.modifier_apply(modifier=mod.name)
    for o in col.objects:
        if o.type=='MESH':repair_surface(o)
    apply_origins(col)
    return scale,all_before,stats(col)


def label(text,x,z,studio_col):
    cu=bpy.data.curves.new('Comparison label','FONT');cu.body=text;cu.size=.17;cu.align_x='CENTER'
    o=bpy.data.objects.new(text,cu);studio_col.objects.link(o);o.location=(x,-2.12,z);o.rotation_euler=(math.pi/2,0,0)
    cu.materials.append(material('Comparison ink',(.72,.78,.88),0,.8,.1));return o


def build(oid):
    p=source_path(oid);bpy.ops.wm.open_mainfile(filepath=str(p));bpy.context.preferences.filepaths.save_version=0
    ref=next(c for c in bpy.data.collections if c.name.startswith('01 MASTER'))
    oldgame=next(c for c in bpy.data.collections if c.name.startswith('02 GAME'))
    keep=set(ref.objects)|set(oldgame.objects)
    for o in list(bpy.data.objects):
        if o not in keep:bpy.data.objects.remove(o,do_unlink=True)
    for c in list(bpy.data.collections):
        if c not in {ref,oldgame}:bpy.data.collections.remove(c)
    ref.name='00 REFERENCE_MASTER_V01';oldgame.name='00 REFERENCE_GAME_V01';ref.hide_render=True;oldgame.hide_render=True
    master=copy_col(ref,'01 MASTER | refined V02');game=copy_col(oldgame,'02 GAME | refined V02')
    s,before,after=refine(master,oid,False);gs,gb,ga=refine(game,oid,True);game.hide_render=True
    for o in game.objects:o.hide_set(True)
    for o in ref.objects:o.hide_set(True)
    for o in oldgame.objects:o.hide_set(True)
    maxh=after['dimensions'][2];target=(0,0,maxh*.45)
    st,cam=studio(target,max(3.8,max(after['dimensions'])*1.22),floor=True)
    bpy.context.scene.cycles.samples=32;bpy.context.scene.cycles.adaptive_threshold=.08
    stem=f'BH_ORE_{oid}_{slug(ORES[oid]["name"])}_V02'
    bpy.ops.wm.save_as_mainfile(filepath=str(ROOT/'models'/f'{stem}.blend'))
    export(game,stem)
    if '--mesh-only' in sys.argv:
        print('MESH_V02_OK',oid,ga,flush=True);return
    for view,loc in [('Front',(0,-7,maxh*.9)),('Iso',(4,-6,maxh*1.15+1.0)),('Back',(0,7,maxh*.9))]:
        render(cam,target,loc,ROOT/'renders'/f'{stem}_{view}.png')
    # A real side-by-side scene: both versions use the same perspective, light and units.
    offset=max(before['dimensions'][0],after['dimensions'][0])*.72
    for o in ref.objects:o.hide_set(False);o.location.x=-offset
    ref.hide_render=False
    for o in master.objects:o.location.x=offset
    labs=[label('V01  /  ANTES',-offset,.025,st),label(f'V02  /  +{(s-1)*100:.1f}%',offset,.025,st)]
    scene=bpy.context.scene;scene.render.resolution_x=1536;scene.render.resolution_y=1024
    cam.data.ortho_scale=max(7.4,after['dimensions'][0]*3.16)
    render(cam,(0,0,maxh*.40),(0,-10,maxh*1.5+1.4),ROOT/'renders'/f'{stem}_Before_After.png')
    for o in master.objects:o.location.x=0
    for o in ref.objects:o.location.x=0;o.hide_set(True)
    ref.hide_render=True
    data={'id':oid,'name':ORES[oid]['name'],'stem':stem,'source':p.name,'nominal_scale':s,'before_master':before,'after_master':after,'before_game':gb,'after_game':ga,'notes':'Original layouts retained; contrast, edge finish, secondary elements and surface-projected seams refined.'}
    (ROOT/'docs'/f'{oid}_V02_Technical.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print('ORE_V02_OK',oid,s,ga['triangles'],flush=True)

if __name__=='__main__':
    args=sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else []
    args=[a for a in args if a!='--mesh-only']
    ids=list(ORES) if args==['--all'] else [args[1]] if len(args)==2 and args[0]=='--id' else args[1].split(',') if len(args)==2 and args[0]=='--ids' else []
    if not ids or any(i not in ORES for i in ids):raise SystemExit('Use -- --id O03, --ids O04,O07 or --all')
    for oid in ids:build(oid)
