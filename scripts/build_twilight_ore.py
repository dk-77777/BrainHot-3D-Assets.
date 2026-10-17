"""Build the Twilight Crystal Ore pilot with Blender 4.3+, no external addons."""
import bpy
import math
import random
from pathlib import Path
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[1]
random.seed(31)
bpy.ops.wm.read_factory_settings(use_empty=True)


def mat(name, color, metallic=0, roughness=.5, emission=0):
    m = bpy.data.materials.new(name)
    m.diffuse_color = (*color, 1)
    m.use_nodes = True
    bs = m.node_tree.nodes.get('Principled BSDF')
    bs.inputs['Base Color'].default_value = (*color, 1)
    bs.inputs['Metallic'].default_value = metallic
    bs.inputs['Roughness'].default_value = roughness
    if emission:
        bs.inputs['Emission Color'].default_value = (*color, 1)
        bs.inputs['Emission Strength'].default_value = emission
    return m

stone = [mat('Basalt | charcoal', (.066,.044,.095), .12,.84),
         mat('Basalt | plum shadow', (.12,.069,.17), .18,.72),
         mat('Basalt | graphite edge', (.20,.17,.23), .24,.61)]
crystal = [mat('Amethyst | dark plum', (.12,.025,.26), .13,.24),
           mat('Amethyst | royal violet', (.26,.055,.58), .10,.20),
           mat('Amethyst | lavender facet', (.52,.24,.79), .06,.16),
           mat('Amethyst | dusk highlight', (.75,.55,.96), .04,.13)]
core_mat = mat('Arcane core | violet', (.50,.19,.91), .1,.22,.9)
crack_mat = mat('Arcane vein | lilac', (.64,.33,1.0), .05,.4,1.8)
bronze = mat('Ornament | aged violet bronze', (.27,.18,.26), .72,.37)
bronze_edge = mat('Ornament | pale bronze', (.52,.34,.45), .65,.33)


def collection(name):
    c = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(c)
    return c

master = collection('01 MASTER | presentation mesh')
mobile = collection('02 GAME | Roblox import')
studio = collection('90 STUDIO | render only')


def link(obj, col):
    for c in list(obj.users_collection): c.objects.unlink(obj)
    col.objects.link(obj)
    return obj


def mesh_obj(name, verts, faces, mats, col, indices=None):
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    obj = bpy.data.objects.new(name, mesh)
    col.objects.link(obj)
    for m in mats: mesh.materials.append(m)
    if indices:
        for p, i in zip(mesh.polygons, indices): p.material_index = i
    return obj


def ring_rock(name, center, radius, height, seed, col, detail=1):
    rng = random.Random(seed)
    n = 11 if detail else 8
    angles = [2*math.pi*i/n for i in range(n)]
    perturb = [rng.uniform(.78,1.18) for _ in range(n)]
    rings = [(0.10,.48),(.34,.93),(.76,1.0),(1.0,.55)] if detail else [(.08,.53),(.52,1.0),(1.0,.55)]
    verts = []
    for zf, rf in rings:
        for i, a in enumerate(angles):
            r=radius*rf*perturb[i]
            verts.append((center[0]+math.cos(a)*r,center[1]+math.sin(a)*r,center[2]+zf*height+rng.uniform(-.045,.045)))
    faces = [tuple(reversed(range(n)))]
    for j in range(len(rings)-1):
        for i in range(n):
            a=j*n+i; b=j*n+(i+1)%n; c=(j+1)*n+(i+1)%n; d=(j+1)*n+i
            if detail and (i+j)%3==0: faces.extend([(a,b,d),(b,c,d)])
            else: faces.append((a,b,c,d))
    faces.append(tuple((len(rings)-1)*n+i for i in range(n)))
    ids=[rng.choice([0,0,0,1,2]) for _ in faces]
    return mesh_obj(name,verts,faces,stone,col,ids)


def shard(name, base, direction, length, width, seed, col, detail=True):
    rng=random.Random(seed)
    axis=Vector(direction).normalized()
    u=axis.cross(Vector((0,1,0)))
    if u.length<.01: u=axis.cross(Vector((1,0,0)))
    u.normalize(); v=axis.cross(u).normalized()
    n=7 if detail else 6
    phase=rng.uniform(0,math.pi)
    levels=[(0,.42),(.13,1),(.70,.78),(1,.07)] if detail else [(0,.50),(.20,1),(1,.06)]
    vertices=[]
    for zf,scale in levels:
        for i in range(n):
            a=phase+i*2*math.pi/n
            rr=width*scale*(1+.12*math.sin(i*7+seed))
            p=Vector(base)+axis*length*zf+rr*(math.cos(a)*u+math.sin(a)*v)
            vertices.append(tuple(p))
    faces=[tuple(reversed(range(n)))]; ids=[0]
    for j in range(len(levels)-1):
        for i in range(n):
            faces.append((j*n+i,j*n+(i+1)%n,(j+1)*n+(i+1)%n,(j+1)*n+i))
            ids.append((i+j+seed)%len(crystal))
    faces.append(tuple((len(levels)-1)*n+i for i in range(n))); ids.append(3)
    return mesh_obj(name,vertices,faces,crystal,col,ids)


def sphere(name, loc, scale, material, col, segments=12, rings=6):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments,ring_count=rings,location=loc)
    o=link(bpy.context.object,col);o.name=name
    o.scale=scale
    bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    o.data.materials.append(material)
    return o


def vein(name, points, radius, material, col, resolution=3):
    curve=bpy.data.curves.new(name,'CURVE');curve.dimensions='3D'
    curve.resolution_u=1;curve.bevel_depth=radius;curve.bevel_resolution=resolution
    spline=curve.splines.new('POLY');spline.points.add(len(points)-1)
    for p,co in zip(spline.points,points): p.co=(*co,1)
    obj=bpy.data.objects.new(name,curve);col.objects.link(obj);obj.data.materials.append(material)
    bpy.ops.object.select_all(action='DESELECT');obj.select_set(True);bpy.context.view_layer.objects.active=obj
    bpy.ops.object.convert(target='MESH')
    return bpy.context.object


def build(col,detail):
    label='MASTER' if detail else 'GAME'
    ring_rock(label+' | main fractured basalt',(0,0,0),1.28,.90,11,col,detail)
    rocks=[(-.96,-.37,.04,.63,.64,12),(.91,.26,.02,.66,.58,13),
           (.30,-.91,.02,.55,.53,14),(-.41,.92,.04,.55,.51,15)]
    for k,(x,y,z,r,h,s) in enumerate(rocks):ring_rock(label+f' | shoulder {k+1}',(x,y,z),r,h,s,col,detail)
    # The core sits in an open rocky socket; the radial crystals create a distinct crown.
    sphere(label+' | arcane heart',(.04,.01,.92),(.30,.29,.34),core_mat,col,16 if detail else 10,8 if detail else 5)
    shards=[((-.17,.08,.57),(-.16,.04,1),1.83,.32,21),
            ((.43,-.16,.57),(.35,-.13,.94),1.44,.27,22),
            ((-.60,-.12,.48),(-.53,-.23,.81),1.24,.26,23),
            ((.02,.48,.51),(.08,.50,.86),1.35,.24,24),
            ((.67,.42,.38),(.70,.24,.67),1.05,.22,25),
            ((-.48,.57,.35),(-.48,.55,.68),.96,.19,26),
            ((.41,-.67,.38),(.32,-.70,.64),.94,.21,27)]
    for k,(pos,d,l,w,s) in enumerate(shards):shard(label+f' | amethyst {k+1:02}',pos,d,l,w,s,col,detail)
    # Bright narrow fissures trace the visible rock, with solid mesh geometry for GLB.
    paths=[ [(-.91,-.40,.67),(-.73,-.36,.83),(-.54,-.29,.92),(-.34,-.21,.95)],
            [(.72,-.68,.62),(.63,-.48,.79),(.48,-.26,.91),(.32,-.10,.94)],
            [(-.17,-1.01,.65),(-.08,-.82,.81),(.05,-.65,.89),(.16,-.47,.93)] ]
    for k,pts in enumerate(paths[:3 if detail else 2]):vein(label+f' | luminous fissure {k+1}',pts,.017 if detail else .023,crack_mat,col,1)
    # Embedded metal bands and little stone chips add craft without shader dependencies.
    for i,(x,y,z) in enumerate([(-.73,-.69,.43),(.84,-.35,.43),(-.70,.57,.46)]):
        sphere(label+f' | bronze seal {i+1}',(x,y,z),(.13,.065,.11),bronze,col,10,5)
        if detail:sphere(label+f' | seal inlay {i+1}',(x,y,z+.045),(.07,.040,.07),bronze_edge,col,8,4)
    if detail:
        for k in range(7):
            a=k*2.399; r=1.16+.08*(k%2)
            ring_rock(label+f' | loose fragment {k+1}',(r*math.cos(a),r*math.sin(a),.03),.18+.03*(k%3),.18,k+41,col,0)
    # Every renderable mesh has identity transforms and shared pivot at origin via mesh data.
    for o in col.objects:
        if o.type=='MESH':
            o.data.transform(o.matrix_world)
            o.matrix_world.identity()

build(master,True);build(mobile,False)

# Save an editable master, including the hidden optimized geometry.
mobile.hide_render=True
world=bpy.data.worlds.new('Twilight Studio World')
bpy.context.scene.world=world
world.color=(.055,.045,.075)
world.use_nodes=True
world.node_tree.nodes['Background'].inputs['Color'].default_value=(.10,.075,.14,1)
world.node_tree.nodes['Background'].inputs['Strength'].default_value=.8

def point_at(obj,target):obj.rotation_euler=(Vector(target)-obj.location).to_track_quat('-Z','Y').to_euler()

for name,loc,power,color,size in [
    ('Key | warm', (3,-4,7),530,(1,.78,.66),4),
    ('Rim | lavender',(-3,2,5),680,(.56,.35,1),3),
    ('Fill | cool',(2,4,3),320,(.38,.57,1),3)]:
    bpy.ops.object.light_add(type='AREA',location=loc);o=link(bpy.context.object,studio);o.name=name
    o.data.energy=power;o.data.color=color;o.data.shape='DISK';o.data.size=size;point_at(o,(0,0,1))

bpy.ops.mesh.primitive_plane_add(size=200,location=(0,0,-.045));floor=link(bpy.context.object,studio);floor.name='Presentation floor'
floor.data.materials.append(mat('Studio | midnight violet',(.043,.033,.072),.12,.47))
bpy.ops.object.camera_add(location=(4,-6,4.2));cam=link(bpy.context.object,studio);cam.name='Render camera';point_at(cam,(0,0,1.04));bpy.context.scene.camera=cam
cam.data.type='ORTHO';cam.data.ortho_scale=4.6
scene=bpy.context.scene
scene.render.engine='CYCLES';scene.cycles.samples=32;scene.cycles.use_denoising=False
scene.render.resolution_x=1024;scene.render.resolution_y=1024;scene.render.resolution_percentage=100
scene.render.image_settings.file_format='PNG'
scene.view_settings.view_transform='AgX'
bpy.context.preferences.filepaths.save_version=0

blend=ROOT/'models/Twilight_Crystal_Ore.blend';blend.parent.mkdir(exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=str(blend))
# Export only optimized mesh objects. No lights, floor, cameras, or Blender shader-only effects.
bpy.ops.object.select_all(action='DESELECT')
for o in mobile.objects:o.hide_set(False);o.select_set(True)
bpy.context.view_layer.objects.active=next(iter(mobile.objects))
glb=ROOT/'exports/Twilight_Crystal_Ore.glb';glb.parent.mkdir(exist_ok=True)
bpy.ops.export_scene.gltf(filepath=str(glb),export_format='GLB',use_selection=True,export_apply=True,export_materials='EXPORT')
for o in mobile.objects:o.hide_set(True)
for name,loc in [('Front',(0,-7,3.3)),('Iso',(5,-6,4.3)),('Back',(0,7,3.3))]:
    cam.location=loc;point_at(cam,(0,0,1.04))
    scene.render.filepath=str(ROOT/'renders'/f'Twilight_Crystal_{name}.png')
    bpy.ops.render.render(write_still=True)
print('BUILD_OK',blend,glb)
