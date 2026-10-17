"""Geometry and presentation helpers. No shared pickaxe head or shaft meshes."""
import bpy, bmesh, math, random
from mathutils import Vector, Matrix
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]


def reset():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.context.preferences.filepaths.save_version=0


def collection(name):
    c=bpy.data.collections.new(name);bpy.context.scene.collection.children.link(c);return c


def material(name,color,metal=0,rough=.5,emit=0):
    m=bpy.data.materials.new(name);m.diffuse_color=(*color,1);m.use_nodes=True
    p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*color,1)
    p.inputs['Metallic'].default_value=metal;p.inputs['Roughness'].default_value=rough
    p.inputs['Emission Color'].default_value=(*color,1);p.inputs['Emission Strength'].default_value=emit
    return m


def move(o,c):
    for old in list(o.users_collection):old.objects.unlink(o)
    c.objects.link(o);return o


def mesh(name,verts,faces,mats,c):
    d=bpy.data.meshes.new(name);d.from_pydata(verts,[],faces);d.update()
    bm=bmesh.new();bm.from_mesh(d);bmesh.ops.recalc_face_normals(bm,faces=bm.faces);bm.to_mesh(d);bm.free()
    o=bpy.data.objects.new(name,d);c.objects.link(o)
    for m in mats:d.materials.append(m)
    return o


def profile(name,outline,depth,m,c,y=0,bevel=.018,edge=None):
    n=len(outline);verts=[(x,y+dy,z) for dy in [-depth/2,depth/2] for x,z in outline]
    faces=[tuple(reversed(range(n))),tuple(range(n,2*n))]+[(i,(i+1)%n,(i+1)%n+n,i+n) for i in range(n)]
    o=mesh(name,verts,faces,[m]+([edge] if edge else []),c)
    if bevel:
        mod=o.modifiers.new('Crafted edge chamfer','BEVEL');mod.width=bevel;mod.segments=2;mod.material=1 if edge else -1
        bpy.context.view_layer.objects.active=o;o.select_set(True)
        bpy.ops.object.modifier_apply(modifier=mod.name);o.select_set(False)
    return o


def path(name,pts,radii,m,c,sides=10):
    vs=[];previous_u=None
    for j,p in enumerate(pts):
        p=Vector(p);axis=Vector(pts[min(j+1,len(pts)-1)])-Vector(pts[max(0,j-1)])
        axis.normalize()
        if previous_u is None:
            reference=Vector((0,1,0)) if abs(axis.y)<.85 else Vector((0,0,1))
            u=axis.cross(reference).normalized()
        else:
            u=previous_u-axis*previous_u.dot(axis)
            if u.length<1e-6:u=axis.cross(Vector((1,0,0)))
            u.normalize()
        previous_u=u.copy();v=axis.cross(u).normalized()
        r=radii[j] if isinstance(radii,(list,tuple)) else radii
        for i in range(sides):
            a=2*math.pi*i/sides;vs.append(tuple(p+r*(math.cos(a)*u+math.sin(a)*v)))
    fs=[tuple(reversed(range(sides)))]
    for j in range(len(pts)-1):
        for i in range(sides):fs.append((j*sides+i,j*sides+(i+1)%sides,(j+1)*sides+(i+1)%sides,(j+1)*sides+i))
    fs.append(tuple((len(pts)-1)*sides+i for i in range(sides)))
    return mesh(name,vs,fs,[m],c)


def line(name,pts,r,m,c):return path(name,pts,r,m,c,6)


def gem(name,center,rx,rz,depth,m,c,seed=1,n=7):
    rng=random.Random(seed);cx,cy,cz=center
    verts=[]
    for y,scale in [(depth*.5,.64),(-depth*.20,1),(-depth*.62,.57)]:
        for i in range(n):
            a=2*math.pi*i/n
            verts.append((cx+rx*scale*math.sin(a)*(1+.06*math.sin(i+seed)),cy+y,cz+rz*scale*math.cos(a)))
    fs=[tuple(reversed(range(n)))]
    for j in range(2):
        for i in range(n):fs.append((j*n+i,j*n+(i+1)%n,(j+1)*n+(i+1)%n,(j+1)*n+i))
    fs.append(tuple(2*n+i for i in range(n)))
    o=mesh(name,verts,fs,m if isinstance(m,list) else [m],c)
    if isinstance(m,list):
        for p in o.data.polygons:p.material_index=(p.index+seed)%len(m)
    return o


def rock(name,loc,scale,m,c,seed=0):
    rng=random.Random(seed)
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1,radius=1,location=loc)
    o=move(bpy.context.object,c);o.name=name
    for v in o.data.vertices:
        v.co*=rng.uniform(.83,1.14)
    o.scale=scale;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    for x in m if isinstance(m,list) else [m]:o.data.materials.append(x)
    for p in o.data.polygons:p.material_index=(p.index+seed)%len(o.data.materials)
    return o


def ring(name,loc,radius,thick,m,c,rotation=(0,0,0),major=20):
    bpy.ops.mesh.primitive_torus_add(major_segments=major,minor_segments=6,location=loc,major_radius=radius,minor_radius=thick,rotation=rotation)
    o=move(bpy.context.object,c);o.name=name;o.data.materials.append(m)
    bpy.ops.object.transform_apply(location=False,rotation=True,scale=True);return o


def apply_origins(c,shift=(0,0,0)):
    for o in c.objects:
        if o.type=='MESH':
            o.data.transform(Matrix.Translation(Vector(shift))@o.matrix_world);o.matrix_world=Matrix.Identity(4)


def clone_game(master):
    c=collection('02 GAME | export')
    for o in master.objects:
        if o.type!='MESH':continue
        d=o.copy();d.data=o.data.copy();c.objects.link(d);d.name=o.name.replace('MASTER','GAME')
        if len(d.data.polygons)>120:
            bpy.context.view_layer.objects.active=d
            mod=d.modifiers.new('Remove coplanar edges','DECIMATE');mod.decimate_type='DISSOLVE';mod.angle_limit=.008
            bpy.ops.object.modifier_apply(modifier=mod.name)
    c.hide_render=True
    for o in c.objects:o.hide_set(True)
    return c


def aim(o,target):o.rotation_euler=(Vector(target)-o.location).to_track_quat('-Z','Y').to_euler()


def studio(target=(0,0,1),ortho=4.6,floor=False):
    c=collection('90 STUDIO | render only')
    world=bpy.data.worlds.new('Studio world');bpy.context.scene.world=world;world.use_nodes=True
    world.node_tree.nodes['Background'].inputs['Color'].default_value=(.10,.12,.17,1)
    world.node_tree.nodes['Background'].inputs['Strength'].default_value=.35
    for name,loc,power,color,size in [('Key',(2,-4,6),470,(1,.87,.72),4),('Rim',(-3,1,4),620,(.46,.65,1),3),('Fill',(3,2,3),250,(1,.67,.4),3)]:
        bpy.ops.object.light_add(type='AREA',location=loc);o=move(bpy.context.object,c);o.name=name
        o.data.energy=power;o.data.color=color;o.data.shape='DISK';o.data.size=size;aim(o,target)
    if floor:
        bpy.ops.mesh.primitive_plane_add(size=200,location=(0,0,-.07));o=move(bpy.context.object,c);o.name='Presentation floor'
        o.data.materials.append(material('Studio floor',(.047,.055,.077),0,.95))
    bpy.ops.object.camera_add(location=(3,-7,3));cam=move(bpy.context.object,c);cam.name='Presentation camera';cam.data.type='ORTHO';cam.data.ortho_scale=ortho;aim(cam,target)
    s=bpy.context.scene;s.unit_settings.system='METRIC';s.unit_settings.scale_length=1;s.camera=cam;s.render.engine='CYCLES';s.cycles.samples=48;s.cycles.use_denoising=False
    s.cycles.use_adaptive_sampling=True;s.cycles.adaptive_threshold=.06;s.cycles.max_bounces=3
    s.cycles.diffuse_bounces=2;s.cycles.glossy_bounces=2;s.cycles.sample_clamp_indirect=2
    s.render.resolution_x=1024;s.render.resolution_y=1024;s.render.resolution_percentage=100
    s.render.image_settings.file_format='PNG';s.view_settings.view_transform='AgX'
    return c,cam


def export(c,stem):
    bpy.ops.object.select_all(action='DESELECT')
    for o in c.objects:o.hide_set(False);o.select_set(True)
    bpy.context.view_layer.objects.active=next(iter(c.objects))
    bpy.ops.export_scene.gltf(filepath=str(ROOT/'exports'/f'{stem}.glb'),export_format='GLB',use_selection=True,export_apply=True,export_materials='EXPORT')
    for o in c.objects:o.hide_set(True)


def render(cam,target,loc,path):
    cam.location=loc;aim(cam,target);bpy.context.scene.render.filepath=str(path);bpy.ops.render.render(write_still=True)


def stats(c):
    objs=[o for o in c.objects if o.type=='MESH'];v=[o.matrix_world@x.co for o in objs for x in o.data.vertices]
    return {'meshes':len(objs),'triangles':sum(len(p.vertices)-2 for o in objs for p in o.data.polygons),'dimensions':[round(max(x[i] for x in v)-min(x[i] for x in v),4) for i in range(3)]}
