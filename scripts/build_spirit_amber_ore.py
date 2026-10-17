"""Build O04 Spirit Amber Ore in Blender 4.3+, with master and game meshes."""
import bpy
import math
import random
from pathlib import Path
from mathutils import Vector

ROOT=Path(__file__).resolve().parents[1]
random.seed(404)
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.context.preferences.filepaths.save_version=0


def material(name, rgb, metal=0, rough=.45, glow=0):
    m=bpy.data.materials.new(name);m.diffuse_color=(*rgb,1);m.use_nodes=True
    p=m.node_tree.nodes.get('Principled BSDF')
    p.inputs['Base Color'].default_value=(*rgb,1)
    p.inputs['Metallic'].default_value=metal
    p.inputs['Roughness'].default_value=rough
    if glow:
        p.inputs['Emission Color'].default_value=(*rgb,1)
        p.inputs['Emission Strength'].default_value=glow
    return m

rock=[material('Slate | umber black',(.065,.045,.052),.1,.87),
      material('Slate | warm brown',(.13,.075,.053),.1,.76),
      material('Slate | carved edge',(.23,.14,.09),.17,.65)]
resin=[material('Amber | burnt umber',(.25,.065,.012),.04,.31),
       material('Amber | deep honey',(.53,.18,.025),.05,.25),
       material('Amber | warm gold',(.83,.39,.055),.04,.19),
       material('Amber | bright facet',(1,.66,.19),.02,.14)]
gold=material('Vein | fossil gold',(.70,.38,.08),.42,.35)
glow=material('Inclusion | captive light',(1,.72,.22),.03,.27,2.0)
rootmat=material('Root | ancient bark',(.17,.085,.045),.04,.91)


def collection(name):
    c=bpy.data.collections.new(name);bpy.context.scene.collection.children.link(c);return c
master=collection('01 MASTER | presentation mesh')
game=collection('02 GAME | Roblox import')
studio=collection('90 STUDIO | render only')


def relink(obj,col):
    for c in list(obj.users_collection):c.objects.unlink(obj)
    col.objects.link(obj);return obj


def mesh(name,verts,faces,mats,col,idx=None):
    data=bpy.data.meshes.new(name);data.from_pydata(verts,[],faces);data.update()
    obj=bpy.data.objects.new(name,data);col.objects.link(obj)
    for m in mats:data.materials.append(m)
    if idx:
        for p,i in zip(data.polygons,idx):p.material_index=i
    return obj


def rock_piece(name,cx,cy,z,r,h,seed,col,detailed):
    rng=random.Random(seed);n=10 if detailed else 8
    angles=[2*math.pi*i/n for i in range(n)]
    jitter=[rng.uniform(.76,1.2) for _ in range(n)]
    levels=[(.0,.67),(.20,1.05),(.60,1),(.98,.72)] if detailed else [(0,.68),(.40,1),(.98,.72)]
    vs=[]
    for zf,rf in levels:
        for i,a in enumerate(angles):
            q=r*rf*jitter[i]
            vs.append((cx+q*math.cos(a),cy+q*math.sin(a),z+h*zf+rng.uniform(-.018,.018)))
    fs=[tuple(reversed(range(n)))];ids=[0]
    for j in range(len(levels)-1):
        for i in range(n):
            fs.append((j*n+i,j*n+(i+1)%n,(j+1)*n+(i+1)%n,(j+1)*n+i));ids.append((seed+i+j)%3)
    fs.append(tuple((len(levels)-1)*n+i for i in range(n)));ids.append(1)
    return mesh(name,vs,fs,rock,col,ids)


def amber_piece(name,loc,height,width,lean,seed,col,detailed):
    rng=random.Random(seed);n=9 if detailed else 7
    # Uneven lobes and a broken ridge make each fossil a unique resin mass.
    sides=[rng.uniform(.82,1.2) for _ in range(n)]
    phase=rng.uniform(-.3,.3)
    levels=[(0,.48,0),(.18,1,.12),(.49,1.08,.32),(.82,.78,.73),(1,.28,1)] if detailed else [(0,.55,0),(.30,1,.2),(.75,.86,.65),(1,.28,1)]
    vs=[]
    for zf,scale,shift in levels:
        for i in range(n):
            a=2*math.pi*i/n+phase
            r=width*scale*sides[i]
            vs.append((loc[0]+r*math.cos(a)+lean[0]*shift,loc[1]+r*math.sin(a)+lean[1]*shift,loc[2]+height*zf+.04*math.sin(a*3+seed)))
    fs=[tuple(reversed(range(n)))];idx=[0]
    for j in range(len(levels)-1):
        for i in range(n):
            fs.append((j*n+i,j*n+(i+1)%n,(j+1)*n+(i+1)%n,(j+1)*n+i))
            idx.append((i*2+j+seed)%len(resin))
    fs.append(tuple((len(levels)-1)*n+i for i in range(n)));idx.append(2)
    return mesh(name,vs,fs,resin,col,idx)


def orb(name,loc,scale,mat,col,n=10,rings=6):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=n,ring_count=rings,location=loc)
    o=relink(bpy.context.object,col);o.name=name;o.scale=scale
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    o.data.materials.append(mat);return o


def tube(name,points,radius,mat,col):
    cu=bpy.data.curves.new(name,'CURVE');cu.dimensions='3D';cu.bevel_depth=radius;cu.bevel_resolution=1
    sp=cu.splines.new('POLY');sp.points.add(len(points)-1)
    for p,xyz in zip(sp.points,points):p.co=(*xyz,1)
    o=bpy.data.objects.new(name,cu);col.objects.link(o);cu.materials.append(mat)
    bpy.ops.object.select_all(action='DESELECT');o.select_set(True);bpy.context.view_layer.objects.active=o
    bpy.ops.object.convert(target='MESH');return bpy.context.object


def build(col,detailed):
    prefix='MASTER' if detailed else 'GAME'
    rock_piece(prefix+' | low slate dais',0,0,0,1.26,.48,1,col,detailed)
    for j,(x,y,r,h) in enumerate([(-.85,-.35,.55,.37),(.88,.22,.52,.43),(-.18,.93,.49,.31),(.32,-.93,.55,.34)]):
        rock_piece(prefix+f' | fractured rim {j+1}',x,y,.03,r,h,j+6,col,detailed)
    chunks=[((-.48,-.25,.38),1.38,.50,(-.11,.04),24),
            ((.42,.24,.37),1.11,.53,(.18,.10),25),
            ((.03,-.69,.34),.79,.34,(.09,-.16),26),
            ((-.60,.52,.33),.80,.31,(-.13,.12),27)]
    for j,(loc,h,w,lean,seed) in enumerate(chunks):
        amber_piece(prefix+f' | fossil resin {j+1}',loc,h,w,lean,seed,col,detailed)
    # Embedded asymmetrical firefly-like seeds, deliberately no insect geometry.
    seeds=[(-.62,-.68,.98),(-.27,-.67,1.33),(.55,-.22,.95),(.75,.08,1.20),(-.38,.16,1.07)]
    for j,p in enumerate(seeds[:5 if detailed else 3]):
        orb(prefix+f' | captive light {j+1}',p,(.083,.037,.10),glow,col,10 if detailed else 8,5)
        if detailed:
            orb(prefix+f' | gold halo {j+1}',(p[0],p[1]+.013,p[2]),(.12,.025,.13),gold,col,10,5)
    # Ribbons of fossilized bark bind the base, adding a distinct material break.
    rootpaths=[ [(-1.05,-.35,.38),(-.83,-.44,.49),(-.61,-.41,.56),(-.39,-.30,.59)],
                [(.80,-.63,.34),(.68,-.47,.49),(.46,-.35,.53),(.30,-.18,.59)],
                [(-.80,.53,.33),(-.61,.65,.46),(-.39,.59,.52)] ]
    for j,path in enumerate(rootpaths[:3 if detailed else 2]):tube(prefix+f' | petrified root {j+1}',path,.055 if detailed else .065,rootmat,col)
    # Metal-like mineral striations are actual meshes, not procedural shaders.
    if detailed:
        for j,path in enumerate([
            [(-.79,-.46,.83),(-.63,-.63,1.00),(-.45,-.58,1.17)],
            [(.18,-.28,.82),(.36,-.36,.99),(.55,-.24,1.14)] ]):
            tube(prefix+f' | amber vein {j+1}',path,.014,gold,col)
    for o in col.objects:
        if o.type=='MESH':o.data.transform(o.matrix_world);o.matrix_world.identity()

build(master,True);build(game,False)
game.hide_render=True
world=bpy.data.worlds.new('Warm twilight studio');bpy.context.scene.world=world;world.use_nodes=True
world.node_tree.nodes['Background'].inputs['Color'].default_value=(.11,.07,.07,1)
world.node_tree.nodes['Background'].inputs['Strength'].default_value=.65

def aim(o,p):o.rotation_euler=(Vector(p)-o.location).to_track_quat('-Z','Y').to_euler()
for name,loc,power,color,size in [
    ('Key | honey',(3,-4,6),650,(1,.74,.43),4),
    ('Rim | cold dusk',(-3,2,5),800,(.48,.54,1),3),
    ('Fill | soft amber',(2,4,3),400,(1,.51,.24),3)]:
    bpy.ops.object.light_add(type='AREA',location=loc);o=relink(bpy.context.object,studio);o.name=name
    o.data.energy=power;o.data.color=color;o.data.shape='DISK';o.data.size=size;aim(o,(0,0,.8))
bpy.ops.mesh.primitive_plane_add(size=200,location=(0,0,-.05));o=relink(bpy.context.object,studio);o.name='Studio floor'
o.data.materials.append(material('Floor | dark aubergine',(.065,.038,.055),.1,.55))
bpy.ops.object.camera_add(location=(4,-6,3.5));cam=relink(bpy.context.object,studio);cam.name='Render camera'
cam.data.type='ORTHO';cam.data.ortho_scale=4.2;aim(cam,(0,0,.82));scene=bpy.context.scene;scene.camera=cam
scene.render.engine='CYCLES';scene.cycles.samples=32;scene.cycles.use_denoising=False
scene.render.resolution_x=1024;scene.render.resolution_y=1024;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG';scene.view_settings.view_transform='AgX'
blend=ROOT/'models/Spirit_Amber_Ore.blend';bpy.ops.wm.save_as_mainfile(filepath=str(blend))
bpy.ops.object.select_all(action='DESELECT')
for o in game.objects:o.hide_set(False);o.select_set(True)
bpy.context.view_layer.objects.active=next(iter(game.objects))
glb=ROOT/'exports/Spirit_Amber_Ore.glb'
bpy.ops.export_scene.gltf(filepath=str(glb),export_format='GLB',use_selection=True,export_apply=True,export_materials='EXPORT')
for o in game.objects:o.hide_set(True)
for name,pos in [('Front',(0,-6,2.9)),('Iso',(4,-6,3.4)),('Back',(0,6,2.9))]:
    cam.location=pos;aim(cam,(0,0,.82))
    scene.render.filepath=str(ROOT/'renders'/f'Spirit_Amber_{name}.png')
    bpy.ops.render.render(write_still=True)
print('BUILD_OK',blend,glb)
