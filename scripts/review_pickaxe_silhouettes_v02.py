"""Render V02 pilots together and measure pairwise silhouette overlap as a QA aid."""
import sys,json,itertools
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from art_v02_common import *
IDS=['P01','P05','P06','P12','P16']
reset();groups={}
for pid in IDS:
    p=next((ROOT/'models').glob(f'BH_PICK_{pid}_*_V02.blend'))
    with bpy.data.libraries.load(str(p),link=False) as (src,dst):dst.collections=[n for n in src.collections if n.startswith('01 MASTER')]
    c=dst.collections[0];bpy.context.scene.collection.children.link(c);c.name=pid+' | independent model';groups[pid]=c
st,cam=studio((0,0,1.0),16.3)
for k,pid in enumerate(IDS):
    for o in groups[pid].objects:o.location.x=(k-2)*3.1
    cu=bpy.data.curves.new(pid+' label','FONT');cu.body=pid;cu.size=.26;cu.align_x='CENTER'
    o=bpy.data.objects.new(pid+' label',cu);st.objects.link(o);o.location=((k-2)*3.1,-.10,-1.12);o.rotation_euler=(math.pi/2,0,0)
    cu.materials.append(material('Label | light',(.78,.83,.9),0,.9,.4))
scene=bpy.context.scene;scene.render.resolution_x=2560;scene.render.resolution_y=1024;scene.cycles.samples=32
render(cam,(0,0,1),(0,-10,1.0),ROOT/'renders/Pickaxe_Pilots_V02_Lineup.png')
black=bpy.data.materials.new('QA | pure silhouette');black.use_nodes=True
nodes=black.node_tree.nodes;nodes.clear();out=nodes.new('ShaderNodeOutputMaterial');em=nodes.new('ShaderNodeEmission');em.inputs[0].default_value=(0,0,0,1);black.node_tree.links.new(em.outputs[0],out.inputs['Surface'])
scene.view_layers[0].material_override=black;scene.view_settings.view_transform='Standard';scene.world.node_tree.nodes['Background'].inputs['Color'].default_value=(1,1,1,1);scene.world.node_tree.nodes['Background'].inputs['Strength'].default_value=1
scene.cycles.samples=8
render(cam,(0,0,1),(0,-10,1),ROOT/'renders/Pickaxe_Pilots_V02_Silhouettes.png')
# Individual masks share the same view, units and grip origin. No labels or aura.
for o in st.objects:
    if o.type=='FONT':o.hide_render=True
scene.render.resolution_x=512;scene.render.resolution_y=512;cam.data.ortho_scale=4.7
for c in groups.values():
    c.hide_render=True
    for o in c.objects:o.location.x=0
masks={}
for pid,c in groups.items():
    c.hide_render=False
    path=ROOT/'renders'/f'{pid}_V02_Silhouette.png'
    render(cam,(0,0,.95),(0,-7,.95),path)
    im=bpy.data.images.load(str(path),check_existing=False);pix=list(im.pixels)
    masks[pid]={i//4 for i in range(0,len(pix),4) if pix[i]<.5}
    bpy.data.images.remove(im);c.hide_render=True
pairs=[]
for a,b in itertools.combinations(IDS,2):
    pairs.append({'a':a,'b':b,'intersection_over_union':round(len(masks[a]&masks[b])/len(masks[a]|masks[b]),4)})
result={'method':'Front orthographic, same units/grip origin, no aura, pure black masks; overlap is an aid, not an artistic approval.','pairs':pairs,'max_overlap':max(p['intersection_over_union'] for p in pairs)}
(ROOT/'docs/Pickaxe_V02_Silhouette_Review.json').write_text(json.dumps(result,indent=2)+'\n')
print('SILHOUETTE_REVIEW',json.dumps(result),flush=True)
if result['max_overlap']>.72:raise RuntimeError('Silhouette overlap requires redesign')
