"""Render four review boards from the actual refined meshes (no image manipulation)."""
import sys,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from art_v02_common import *
from mathutils import Matrix
for page in range(4):
    reset()
    for j in range(6):
        oid=f'O{page*6+j+1:02}';p=next((ROOT/'models').glob(f'BH_ORE_{oid}_*_V02.blend'))
        with bpy.data.libraries.load(str(p),link=False) as (src,dst):dst.collections=[n for n in src.collections if n.startswith('01 MASTER')]
        c=dst.collections[0];bpy.context.scene.collection.children.link(c)
        x=(j%3-1)*3.75;z=(1-j//3)*4.0
        rotation=Matrix.Rotation(math.radians(23),4,'X')@Matrix.Rotation(math.radians(28),4,'Z')
        for o in c.objects:o.matrix_world=Matrix.Translation((x,0,z))@rotation
        cu=bpy.data.curves.new(oid+' label','FONT');cu.body=oid;cu.size=.21;cu.align_x='CENTER'
        text=bpy.data.objects.new(oid+' label',cu);bpy.context.scene.collection.objects.link(text)
        text.location=(x,-2.5,z-.75);text.rotation_euler=(math.pi/2,0,0)
        cu.materials.append(material('Board label',(.80,.85,.95),0,.8,.6))
    st,cam=studio((0,0,3.0),11.8);scene=bpy.context.scene
    for lamp in st.objects:
        if lamp.type=='LIGHT':lamp.location*=2;lamp.data.energy*=4;lamp.data.size*=2
    scene.render.resolution_x=2048;scene.render.resolution_y=1536;scene.cycles.samples=32
    render(cam,(0,0,3.0),(0,-14,3.0),ROOT/'renders'/f'Ores_V02_Board_{page+1}.png')
    print('ORE_BOARD_OK',page+1,flush=True)
