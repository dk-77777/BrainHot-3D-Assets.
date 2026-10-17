"""Build individual O-series ores and P-series pickaxes from the production manifests.

Usage: blender -b -t 4 --python scripts/build_catalog.py -- --id O01
       blender -b -t 4 --python scripts/build_catalog.py -- --all
Blender 4.3.2; no external addons. O03 and O04 are preserved as earlier pilots.
"""
import bpy
import json
import math
import random
import re
import sys
from pathlib import Path
from mathutils import Vector

ROOT=Path(__file__).resolve().parents[1]
ORES={r['id']:r for r in json.loads((ROOT/'data/24_minerios.json').read_text())}
PICKS={r['id']:r for r in json.loads((ROOT/'data/28_picaretas.json').read_text())}
PALETTES={
'O01':((.13,.17,.20),(.35,.56,.62)),'O02':((.52,.18,.035),(.98,.48,.08)),
'O05':((.12,.15,.17),(.11,.64,.72)),'O06':((.26,.08,.32),(.79,.40,.85)),
'O07':((.46,.50,.55),(.70,.82,.91)),'O08':((.04,.20,.29),(.28,.74,.88)),
'O09':((.03,.11,.32),(.18,.40,.92)),'O10':((.31,.58,.73),(.70,.91,1)),
'O11':((.09,.06,.17),(.52,.17,.81)),'O12':((.23,.11,.17),(.98,.37,.25)),
'O13':((.17,.13,.12),(.86,.32,.08)),'O14':((.28,.09,.03),(.95,.43,.06)),
'O15':((.055,.05,.075),(.65,.15,.22)),'O16':((.33,.015,.025),(.93,.10,.08)),
'O17':((.07,.04,.065),(.83,.18,.25)),'O18':((.19,.055,.035),(.87,.12,.045)),
'O19':((.09,.09,.15),(.40,.30,.72)),'O20':((.11,.08,.22),(.48,.72,.85)),
'O21':((.025,.025,.04),(.27,.22,.48)),'O22':((.08,.06,.26),(.54,.40,.91)),
'O23':((.07,.07,.15),(.59,.47,.83)),'O24':((.12,.08,.24),(.93,.67,.21)),
}
PICK_ACCENTS=[(.32,.71,.82),(.86,.41,.15),(.95,.50,.08),(.36,.65,.86),(.69,.32,.85),(.35,.89,.91),(.56,.72,.96),(.27,.43,.90),(.46,.76,.27),(.54,.83,.96),(.63,.52,.36),(.98,.33,.08),(.63,.35,.82),(.80,.87,.94),(.50,.93,.77),(.54,.32,.95),(.60,.32,.87),(.88,.13,.19),(.96,.72,.27),(.38,.75,.90),(.20,.85,.59),(.17,.83,.79),(.96,.42,.07),(.83,.26,.58),(.80,.88,.93),(.59,.32,.81),(.94,.38,.12),(.90,.70,.30)]


def slug(name):
    import unicodedata
    s=unicodedata.normalize('NFKD',name).encode('ascii','ignore').decode('ascii')
    return re.sub(r'[^A-Za-z0-9]+','_',s).strip('_')


def mat(name,c,metal=0,rough=.45,emission=0):
    m=bpy.data.materials.new(name);m.diffuse_color=(*c,1);m.use_nodes=True
    p=m.node_tree.nodes.get('Principled BSDF')
    p.inputs['Base Color'].default_value=(*c,1)
    p.inputs['Metallic'].default_value=metal
    p.inputs['Roughness'].default_value=rough
    if emission:
        p.inputs['Emission Color'].default_value=(*c,1)
        p.inputs['Emission Strength'].default_value=emission
    return m


def col(name):
    c=bpy.data.collections.new(name);bpy.context.scene.collection.children.link(c);return c


def relink(o,c):
    for old in list(o.users_collection):old.objects.unlink(o)
    c.objects.link(o);return o


def mesh(name,verts,faces,mats,c,indices=None):
    d=bpy.data.meshes.new(name);d.from_pydata(verts,[],faces);d.update()
    o=bpy.data.objects.new(name,d);c.objects.link(o)
    for m in mats:d.materials.append(m)
    if indices:
        for p,i in zip(d.polygons,indices):p.material_index=i
    return o


def loft(name,center,levels,n,mats,c,seed=0,shape=None):
    """Irregular ring loft. levels = (z, x_radius, y_radius, x_shift, y_shift)."""
    rng=random.Random(seed)
    phase=rng.uniform(0,.4);jitter=[rng.uniform(.82,1.17) for _ in range(n)]
    verts=[]
    for z,rx,ry,sx,sy in levels:
        for i in range(n):
            a=phase+2*math.pi*i/n
            r=jitter[i]*(1+.045*math.sin(seed+i*3))
            verts.append((center[0]+sx+rx*r*math.cos(a),center[1]+sy+ry*r*math.sin(a),center[2]+z))
    faces=[tuple(reversed(range(n)))];idx=[0]
    for j in range(len(levels)-1):
        for i in range(n):
            faces.append((j*n+i,j*n+(i+1)%n,(j+1)*n+(i+1)%n,(j+1)*n+i))
            idx.append((i+j+seed)%len(mats))
    faces.append(tuple((len(levels)-1)*n+i for i in range(n)));idx.append((seed+2)%len(mats))
    return mesh(name,verts,faces,mats,c,idx)


def faceted_rock(name,loc,r,h,mats,c,seed,low):
    return loft(name,loc,[(0,.65*r,.57*r,0,0),(.25*h,r,.83*r,0,0),(.74*h,.91*r,.78*r,.04,0),(h,.60*r,.53*r,.02,0)],8 if low else 11,mats,c,seed)


def spire(name,loc,height,width,lean,mats,c,seed,low,tip=.04):
    return loft(name,loc,[(0,.44*width,.44*width,0,0),(.22*height,width,.82*width,.04*lean[0],.04*lean[1]),(.72*height,.77*width,.68*width,.64*lean[0],.64*lean[1]),(height,tip,tip,lean[0],lean[1])],6 if low else 8,mats,c,seed)


def orb(name,loc,scale,m,c,n=10):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=n,ring_count=6,location=loc)
    o=relink(bpy.context.object,c);o.name=name;o.scale=scale
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    o.data.materials.append(m);return o


def tube(name,points,r,m,c):
    cu=bpy.data.curves.new(name,'CURVE');cu.dimensions='3D';cu.bevel_depth=r;cu.bevel_resolution=1
    s=cu.splines.new('POLY');s.points.add(len(points)-1)
    for p,xyz in zip(s.points,points):p.co=(*xyz,1)
    o=bpy.data.objects.new(name,cu);c.objects.link(o);cu.materials.append(m)
    bpy.ops.object.select_all(action='DESELECT');o.select_set(True);bpy.context.view_layer.objects.active=o
    bpy.ops.object.convert(target='MESH');return bpy.context.object


def beam(name,a,b,width,depth,m,c,tip=.08):
    axis=Vector(b)-Vector(a);w=axis.normalized().cross(Vector((0,1,0)))
    if w.length<.05:w=axis.normalized().cross(Vector((1,0,0)))
    w.normalize();v=axis.normalized().cross(w).normalized()
    aa=Vector(a);bb=Vector(b)
    vs=[]
    for p,scale in [(aa,1),(bb,tip)]:
        for u,t in [(-1,-1),(-1,1),(1,1),(1,-1)]:vs.append(tuple(p+u*w*width*scale+t*v*depth*scale))
    fs=[(3,2,1,0)]+[(i,(i+1)%4,(i+1)%4+4,i+4) for i in range(4)]+[(4,5,6,7)]
    return mesh(name,vs,fs,[m],c)


def ring(name,loc,major,minor,mat,c,rotation=None,segments=18):
    bpy.ops.mesh.primitive_torus_add(major_segments=segments,minor_segments=6,
        location=loc,major_radius=major,minor_radius=minor)
    o=relink(bpy.context.object,c);o.name=name
    if rotation:o.rotation_euler=rotation
    bpy.ops.object.transform_apply(location=False,rotation=True,scale=True)
    o.data.materials.append(mat);return o


def build_ore(rec,c,low,materials):
    oid=rec['id'];seed=int(oid[1:]);rng=random.Random(seed)
    dark,mid,accent,light,metal=materials
    base=[dark,mid]
    faceted_rock('Bedrock | primary',(0,0,0),1.20,.40,base,c,seed,low)
    for i,(x,y,r) in enumerate([(-.77,-.34,.48),(.78,.12,.53),(.05,.82,.42)]):
        faceted_rock(f'Bedrock | shoulder {i+1}',(x,y,.015),r,.28,base,c,seed+i+21,low)
    def shards(count,h=1.25,w=.30,arrangement='radial',radius=.56,colors=None):
        for i in range(count):
            a=2*math.pi*i/count+.22*seed
            x=radius*math.cos(a);y=radius*math.sin(a)
            lean=(.25*math.cos(a),.25*math.sin(a)) if arrangement=='radial' else (0,0)
            spire(f'{oid} | shard {i+1}',(x,y,.32),h*(.76+.16*(i%3)),w*(.84+.12*(i%4)),lean,colors or [mid,accent,light],c,seed*11+i,low)
    def stones(count=5):
        for i in range(count):
            a=2*math.pi*i/count+.3
            faceted_rock(f'{oid} | fractured stone {i+1}',(.67*math.cos(a),.58*math.sin(a),.27),.32+.06*(i%3),.39+.13*(i%2),[dark,mid],c,seed*7+i,low)
    if oid in {'O01','O13','O18'}:
        stones(7)
        if oid=='O01':
            for i in range(3):
                x=-.58+i*.49
                tube(f'{oid} | blue mist fissure {i+1}',[(x,-.52,.64),(x+.08,-.37,.71),(x+.16,-.22,.73)],.016,accent,c)
        else:
            for i in range(3):
                x=-.65+i*.46
                tube(f'{oid} | molten seam {i+1}',[(x,-.62,.58),(x+.12,-.29,.69),(x+.2,.06,.70)],.018,accent,c)
        if oid=='O18':shards(3,.69,.20,colors=[dark,mid,accent])
    elif oid=='O02':
        loft('Pumpkin quartz | broad six faces',(0,0,.35),[(0,.45,.45,0,0),(.27,.89,.80,0,0),(.72,.74,.72,0,0),(1.0,.08,.08,0,0)],6,[mid,accent,light],c,seed)
        spire('Triangular heart',(0,-.57,.44),.73,.28,(0,-.14),[mid,accent,light],c,21,low)
        tube('Fossil vine',[(-.74,.24,.36),(-.43,.51,.63),(-.18,.48,1.05)],.045,dark,c)
    elif oid=='O05':
        for i in range(6):
            a=2*math.pi*i/6
            loc=(.62*math.cos(a),.62*math.sin(a),.36)
            loft(f'Rune slab {i+1}',loc,[(0,.24,.17,0,0),(.70,.20,.13,0,0),(.84,.16,.10,0,0)],5,[dark,mid],c,i+seed)
            tube(f'Rune line {i+1}',[(loc[0],loc[1]-.145,.60),(loc[0],loc[1]-.15,.90)],.016,accent,c)
    elif oid=='O06':
        for i,(x,y,lx,ly) in enumerate([(-.56,-.45,-.28,-.15),(.52,.43,.26,.22),(-.45,.43,-.25,.23),(.50,-.45,.26,-.22)]):
            spire(f'X amethyst {i+1}',(x,y,.34),1.23,.25,(lx,ly),[mid,accent,light],c,i+seed,low)
    elif oid=='O07':
        faceted_rock('Moonstone dome',(0,0,.27),.89,.86,[mid,light],c,seed,low)
        for i in range(3 if low else 5):
            a=2*math.pi*i/5;ring(f'Crater rim {i+1}',(.51*math.cos(a),.47*math.sin(a),.93),.09,.024,dark,c,segments=12)
    elif oid in {'O08','O10','O14','O16','O22','O24'}:
        params={'O08':(5,1.65,.22),'O10':(6,1.48,.27),'O14':(9,.79,.21),'O16':(6,1.13,.29),'O22':(6,1.36,.25),'O24':(7,1.22,.29)}
        count,h,w=params[oid];shards(count,h,w)
        if oid in {'O22','O24'}:
            spire('Hero prism',(0,0,.42),2.1,.38,(.07,-.06),[mid,accent,light],c,91,low)
        if oid=='O10':
            for i in range(3):beam(f'Curved ice barb {i+1}',(.42*math.cos(i*2.1),.42*math.sin(i*2.1),.75),(.9*math.cos(i*2.1),.9*math.sin(i*2.1),1.2),.12,.09,light,c)
    elif oid=='O09':
        stones(3)
        for i in range(4):orb(f'Sapphire dodeca-like core {i+1}',(.45*math.cos(i*1.6),.45*math.sin(i*1.6),.75+.12*(i%2)),(.28,.27,.32),accent,c,8)
    elif oid in {'O11','O17','O23'}:
        ring('Enclosing stone / obsidian halo',(0,0,1.02),.72,.13,dark,c,rotation=(math.pi/2,0,0),segments=18)
        if oid=='O23':
            for a in [-.35,.35]:beam('Crossed axis',(a,-.12,.45),(-a,.12,1.52),.13,.12,mid,c)
        elif oid=='O17':loft('Square infernal core',(0,0,.69),[(0,.26,.26,0,0),(.7,.24,.24,0,0)],4,[mid,accent,light],c,10)
        else:orb('Eclipse disk',(0,0,1.04),(.50,.14,.51),accent,c,14)
    elif oid=='O12':
        # Two lobes taper into an angular point, forming a heart from broad facets.
        for i,x in enumerate([-.28,.28]):orb(f'Heart upper lobe {i+1}',(x,0,1.15),(.41,.27,.42),accent,c,10)
        spire('Heart lower point',(0,0,.51),.97,.42,(0,0),[mid,accent,light],c,44,low)
    elif oid in {'O15','O21'}:
        if oid=='O21':loft('Nullstone monolith',(0,0,.31),[(0,.42,.37,0,0),(.77,.45,.39,0,0),(1.4,.38,.34,0,0),(1.62,.15,.13,0,0)],6,[dark,mid],c,3)
        else:
            for i in range(5):
                a=2*math.pi*i/5;beam(f'Ritual obsidian blade {i+1}',(.4*math.cos(a),.4*math.sin(a),.42),(.92*math.cos(a),.92*math.sin(a),1.37),.16,.10,dark,c)
        for i in range(3):tube(f'Deep inscription {i+1}',[(-.24+i*.22,-.42,.77),(-.22+i*.22,-.45,1.28)],.011,accent,c)
    elif oid in {'O19','O20'}:
        for i in range(5):
            a=2*math.pi*i/5
            loc=(.57*math.cos(a),.57*math.sin(a),.51+.13*(i%3))
            loft(f'Anomaly block {i+1}',loc,[(0,.23,.18,0,0),(.45,.20,.18,.07,-.04)],5,[dark,mid,accent],c,seed+i)
        if oid=='O20':spire('Linked anomaly prism',(0,0,.52),1.44,.32,(.10,.08),[mid,accent,light],c,seed,low)
    if oid in {'O01','O13','O14','O15','O16','O18'}:
        for i in range(3 if not low else 2):
            a=i*2.1+.8
            faceted_rock(f'Loose chip {i+1}',(1.1*math.cos(a),1.0*math.sin(a),.02),.16,.14,[dark,mid],c,seed+i+70,low)


def build_pick(rec,c,low,mats):
    pid=rec['id'];index=int(pid[1:]);rng=random.Random(index)
    dark,mid,accent,light,metal=mats
    # Grip origin is at world origin, aligned to local +Z. Head crosses X near Z=2.05.
    wood=mat('Handle | chestnut',(.16,.075,.038),.03,.79)
    shaft=wood if index in {1,2,3,9,23,25} else dark
    loft('Handle | shaped shaft',(0,0,0),[(0,.115,.105,0,0),(.20,.13,.11,0,0),(1.38,.11,.10,0,0),(2.12,.14,.12,0,0)],8 if low else 10,[shaft,dark],c,index)
    ring('Handle | pommel',(0,0,.10),.12,.04,metal,c,segments=12)
    for i,z in enumerate([.32,.48,1.42,1.58,1.83]):
        if low and i in (1,3):continue
        ring(f'Handle | binding {i+1}',(0,0,z),.115,.018,metal,c,segments=12)
    # 28 tuned head profiles: all retain opposing mining tips, with silhouette variation.
    span=[.80,.87,.92,.83,1.02,.95,1.07,.96,.92,1.01,.94,1.04,1.16,.92,1.03,1.08,1.11,1.14,.98,1.03,.90,1.00,1.13,1.21,1.02,1.09,1.21,1.18][index-1]
    width=.18+(.04 if index in {7,11,18,23,27,28} else 0)
    beam('Head | main crossbar',(-.45,0,2.08),(.45,0,2.08),width,.17,dark if index in {1,7,11,15,16,25} else metal,c,tip=1)
    upward=.17 if index in {5,13,18,24} else (-.08 if index in {7,11,23} else .04)
    for side in [-1,1]:
        a=(side*.37,0,2.09);b=(side*span,0,2.09+upward*(1 if side>0 else -.3))
        beam(f'Head | mining tooth {"L" if side<0 else "R"}',a,b,.19 if index<10 else .22,.14,accent,c,tip=.03)
        if index in {5,9,13,18,24,27,28}:
            beam(f'Head | hooked spur {side}',(side*.64,0,2.1),(side*(span-.06),0,1.72),.11,.095,mid,c,tip=.02)
    # Family-specific ornament is placed at a visible central socket.
    if index in {3,23}:orb('Core | carved harvest lantern',(0,-.17,2.12),(.30,.19,.25),accent,c,10)
    elif index in {7,11}:
        for side in [-1,1]:faceted_rock(f'Head | lunar slab {side}',(side*.35,0,1.98),.34,.33,[dark,mid],c,index+side+2,low)
    elif index in {17,26,28}:ring('Head | arcane frame',(0,-.12,2.10),.31,.047,metal,c,rotation=(math.pi/2,0,0),segments=16)
    elif index in {21,22}:
        for i in range(3):tube(f'Core | code trace {i+1}',[(-.15+i*.15,-.19,1.97),(-.10+i*.15,-.20,2.19)],.015,accent,c)
    elif index in {4,8,10,14,16,19,20,25}:
        spire('Head | inset mineral',(0,-.18,1.95),.44,.17,(0,-.04),[mid,accent,light],c,index+38,low)
    else:orb('Core | socket gem',(0,-.18,2.09),(.22,.09,.23),accent,c,10)
    if index in {5,13,18,24}:
        # Scythe family stays a pick: long arcing back blade and a distinct opposing tooth.
        beam('Head | crescent back',(span*.73,0,2.25),(span*.96,.02,2.72),.14,.1,accent,c)
    if index in {27,28}:
        for side in [-1,1]:spire(f'Head | dragon horn {side}',(side*.33,0,2.14),.66,.17,(side*.10,0),[dark,accent,light],c,index*3+side,low)
    if not low:
        for i in range(3):
            z=.63+.22*i
            tube(f'Handle | filigree {i+1}',[(.103,-.025,z),(.108,.02,z+.09),(.09,.05,z+.16)],.012,metal,c)


def aim(obj,target):obj.rotation_euler=(Vector(target)-obj.location).to_track_quat('-Z','Y').to_euler()


def build_one(asset_id):
    is_ore=asset_id.startswith('O');rec=(ORES if is_ore else PICKS)[asset_id]
    bpy.ops.wm.read_factory_settings(use_empty=True);bpy.context.preferences.filepaths.save_version=0
    dark_rgb,acc_rgb=(PALETTES[asset_id] if is_ore else ((.10,.08,.09),PICK_ACCENTS[int(asset_id[1:])-1]))
    mid_rgb=tuple(min(.95,a*.48+b*.52) for a,b in zip(dark_rgb,acc_rgb))
    light_rgb=tuple(min(1,x*.50+.50) for x in acc_rgb)
    dark=mat('Body | dark',dark_rgb,.1,.78)
    mid=mat('Body | mid',mid_rgb,.12,.50)
    accent=mat('Hero material | '+rec['name'],acc_rgb,.09,.25)
    light=mat('Facet | light',light_rgb,.05,.20)
    metal=mat('Craft | antique metal',(.37,.26,.21),.65,.37)
    materials=[dark,mid,accent,light,metal]
    master=col('01 MASTER | detailed');game=col('02 GAME | optimized');studio=col('90 STUDIO | presentation')
    for c,low in [(master,False),(game,True)]:
        if is_ore:build_ore(rec,c,low,materials)
        else:build_pick(rec,c,low,materials)
        for o in c.objects:
            if o.type=='MESH':o.data.transform(o.matrix_world);o.matrix_world.identity()
    game.hide_render=True
    world=bpy.data.worlds.new('Catalogue studio');bpy.context.scene.world=world;world.use_nodes=True
    world.node_tree.nodes['Background'].inputs['Color'].default_value=(.065,.065,.085,1)
    world.node_tree.nodes['Background'].inputs['Strength'].default_value=.8
    for name,loc,power,color,size in [('Key',(3,-4,6),570,(1,.82,.67),4),('Rim',(-3,2,5),680,(.53,.64,1),3),('Fill',(2,4,3),330,(1,.73,.52),3)]:
        bpy.ops.object.light_add(type='AREA',location=loc);o=relink(bpy.context.object,studio);o.name=name
        o.data.energy=power;o.data.color=color;o.data.shape='DISK';o.data.size=size;aim(o,(0,0,1))
    if is_ore:
        bpy.ops.mesh.primitive_plane_add(size=200,location=(0,0,-.055));o=relink(bpy.context.object,studio);o.name='Studio floor';o.data.materials.append(mat('Floor | plum charcoal',(.052,.045,.065),.1,.55))
    bpy.ops.object.camera_add(location=(3,-6,3.3));camera=relink(bpy.context.object,studio);camera.name='Render camera'
    camera.data.type='ORTHO';camera.data.ortho_scale=4.2 if is_ore else 3.8
    scene=bpy.context.scene;scene.camera=camera
    scene.render.engine='CYCLES';scene.cycles.samples=20;scene.cycles.use_denoising=False;scene.render.resolution_x=1024;scene.render.resolution_y=1024;scene.render.resolution_percentage=100
    scene.render.image_settings.file_format='PNG';scene.view_settings.view_transform='AgX'
    target=(0,0,.8 if is_ore else 1.25)
    aim(camera,target)
    stem=f'BH_{"ORE" if is_ore else "PICK"}_{asset_id}_{slug(rec["name"])}_V01'
    model=ROOT/'models'/f'{stem}.blend';glb=ROOT/'exports'/f'{stem}.glb'
    bpy.ops.wm.save_as_mainfile(filepath=str(model))
    bpy.ops.object.select_all(action='DESELECT')
    for o in game.objects:o.hide_set(False);o.select_set(True)
    bpy.context.view_layer.objects.active=next(iter(game.objects))
    bpy.ops.export_scene.gltf(filepath=str(glb),export_format='GLB',use_selection=True,export_apply=True,export_materials='EXPORT')
    for o in game.objects:o.hide_set(True)
    for view,loc in [('Front',(0,-6,2.8 if is_ore else 1.7)),('Iso',(4,-6,3.5 if is_ore else 2.3)),('Back',(0,6,2.8 if is_ore else 1.7))]:
        camera.location=loc;aim(camera,target)
        scene.render.filepath=str(ROOT/'renders'/f'{stem}_{view}.png')
        bpy.ops.render.render(write_still=True)
    triangles=sum(len(p.vertices)-2 for o in game.objects if o.type=='MESH' for p in o.data.polygons)
    print('ASSET_OK',asset_id,stem,'triangles',triangles,flush=True)


def main():
    argv=sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else []
    if len(argv)==2 and argv[0]=='--id':ids=[argv[1]]
    elif argv==['--all']:ids=[i for i in ORES if i not in {'O03','O04'}]+list(PICKS)
    else:raise SystemExit('Use -- --id O01 or -- --all')
    for a in ids:
        if a in {'O03','O04'}:raise SystemExit('Existing pilots must not be replaced')
        build_one(a)

if __name__=='__main__':main()
