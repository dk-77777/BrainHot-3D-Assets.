"""Five individually designed pickaxes. Run with -- --id P01 or -- --all."""
import sys,math,json,random
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from art_v02_common import *
NAMES={'P01':'Picareta_Runica_de_Pedra','P05':'Colheita_Sombria','P06':'Presa_Espectral','P12':'Picareta_de_Magma_Profano','P16':'Fragmento_Void'}


def stone(c):
    slate=material('P01 | blue slate',(.095,.13,.16),.08,.86)
    edge=material('P01 | chipped slate edges',(.29,.34,.37),.10,.67)
    wood=material('P01 | chestnut grain',(.16,.065,.025),0,.88)
    leather=material('P01 | weathered leather',(.075,.045,.026),0,.91)
    iron=material('P01 | oxidized iron',(.18,.16,.14),.58,.67)
    rope=material('P01 | flax cord',(.43,.31,.18),0,.95)
    rune=material('P01 | restrained cyan rune',(.15,.62,.72),.05,.5,.45)
    profile('P01 | carved double-tooth slate',[(-1.05,2.25),(-.78,2.64),(-.49,2.71),(-.34,2.61),(-.10,2.67),(.12,2.61),(.34,2.64),(.58,2.55),(1.06,2.16),(.69,2.30),(.45,2.35),(.28,2.31),(.06,2.24),(-.21,2.31),(-.38,2.40),(-.76,2.43)],.36,slate,c,bevel=.035,edge=edge)
    profile('P01 | split stone face',[(-.70,2.54),(-.42,2.62),(-.23,2.51),(-.34,2.42),(-.63,2.47)],.018,edge,c,y=-.193,bevel=.003)
    path('P01 | crooked chestnut haft',[(.04,0,0),(-.04,.01,.38),(.03,0,.92),(-.055,.02,1.53),(0,0,2.51)],[.14,.15,.12,.135,.17],wood,c,12)
    for i in range(7):
        z=.22+i*.105
        ring(f'P01 | grip leather wrap {i}',(-.015,0,z),.145,.022,leather,c,major=14)
    profile('P01 | wooden locking wedge',[(-.13,2.37),(.13,2.37),(.10,2.73),(-.10,2.73)],.15,wood,c,y=.08,bevel=.018)
    for side in [-1,1]:
        line('P01 | diagonal lashing',[(side*.21,-.225,2.29),(-side*.18,-.23,2.58)],.023,rope,c)
        rock('P01 | iron rivet',(side*.30,-.214,2.53),(.045,.028,.045),iron,c,side+3)
    line('P01 | rune stem',[(0,-.229,2.34),(0,-.232,2.58)],.012,rune,c)
    for side in [-1,1]:line('P01 | rune branch',[(0,-.233,2.45),(side*.085,-.234,2.52)],.012,rune,c)
    ring('P01 | iron pommel',(0,0,.06),.145,.033,iron,c,major=12)
    return rune


def harvest(c):
    bark=material('P05 | charred living wood',(.055,.035,.035),.03,.89)
    metal=material('P05 | harvest iron',(.11,.12,.095),.55,.43)
    bronze=material('P05 | worn pumpkin bronze',(.39,.20,.065),.64,.38)
    edge=material('P05 | sharpened warm steel',(.50,.42,.26),.74,.28)
    amber=material('P05 | heart amber',(.95,.32,.035),.04,.22,.5)
    amberlight=material('P05 | amber crown facet',(1,.62,.13),.05,.20,.5)
    leaf=material('P05 | dried autumn leaf',(.43,.16,.035),0,.83)
    green=material('P05 | spectral vine',(.22,.72,.22),.03,.5,.5)
    profile('P05 | long reaping talon',[(-.17,2.31),(-.48,2.43),(-.84,2.69),(-1.22,2.81),(-1.45,2.71),(-1.25,3.03),(-.93,3.10),(-.62,2.96),(-.35,2.72),(-.10,2.67)],.20,metal,c,bevel=.025,edge=bronze)
    profile('P05 | long talon cutting edge',[(-.48,2.43),(-.84,2.69),(-1.22,2.81),(-1.45,2.71),(-1.15,2.92),(-.82,2.80)],.025,edge,c,y=-.115,bevel=.008)
    profile('P05 | opposing hook',[(.08,2.35),(.42,2.40),(.68,2.21),(.91,1.83),(1.00,2.23),(.81,2.60),(.48,2.80),(.13,2.68)],.25,metal,c,bevel=.028,edge=bronze)
    profile('P05 | short hook edge',[(.53,2.42),(.68,2.21),(.91,1.83),(.84,2.32),(.66,2.52)],.025,edge,c,y=-.145,bevel=.008)
    path('P05 | twisted root haft',[(.02,.02,0),(-.13,.04,.36),(-.19,0,.78),(.04,.02,1.18),(.16,.04,1.62),(-.07,0,2.02),(0,0,2.62)],[.12,.16,.145,.12,.15,.17,.18],bark,c,11)
    path('P05 | split root strand',[(-.10,-.03,.21),(.04,-.10,.68),(-.06,-.08,1.12),(-.18,-.03,1.48),(-.11,-.05,1.99)],[.035,.045,.04,.05,.025],bronze,c,7)
    for i,(x,z,side) in enumerate([(-.16,.67,-1),(.13,1.55,1),(-.08,1.94,-1)]):
        profile(f'P05 | bark thorn {i}',[(x,z),(x+side*.24,z+.17),(x+side*.07,z+.24)],.10,bark,c,bevel=.012)
    gem('P05 | amber heart',(0,-.17,2.55),.30,.29,.26,[amber,amberlight],c,5,8)
    for i in range(5):
        x=(i-2)*.105
        line(f'P05 | pumpkin cage rib {i}',[(x*.65,-.23,2.83),(x,-.35,2.68),(x*.95,-.35,2.49),(x*.45,-.24,2.30)],.017,bronze,c)
    path('P05 | crown stem',[(.02,-.09,2.79),(-.02,-.10,2.94),(.08,-.08,2.98)],[.045,.038,.015],bark,c,8)
    for i in range(3):
        x=-.23+i*.24;z=1.2+i*.31
        profile('P05 | dry leaf',[(x,z),(x-.12,z+.11),(x-.07,z+.30),(x+.05,z+.22),(x+.10,z+.07)],.018,leaf,c,y=-.07,bevel=.005)
    line('P05 | vine of harvest',[(-.20,-.13,.72),(-.08,-.14,1.1),(.13,-.12,1.45),(.07,-.17,1.8),(-.10,-.16,2.10)],.015,green,c)
    return green


def spectral(c):
    silver=material('P06 | tarnished moon silver',(.30,.42,.47),.78,.32)
    edge=material('P06 | polished silver edge',(.66,.82,.85),.73,.20)
    blue=material('P06 | deep blue leather',(.018,.065,.105),.03,.78)
    cyan=material('P06 | cyan spectral crystal',(.08,.53,.67),.10,.20,.2)
    pale=material('P06 | milky crystal facet',(.44,.89,.92),.05,.15,.25)
    soul=material('P06 | soul light',(.16,.88,.92),.03,.2,1.0)
    profile('P06 | descending lunar fang',[(-.07,2.42),(-.47,2.50),(-.88,2.40),(-1.20,2.13),(-1.36,1.73),(-1.29,2.34),(-.99,2.73),(-.53,2.93),(-.12,2.81)],.13,silver,c,bevel=.020,edge=edge)
    profile('P06 | descending cyan blade',[(-.37,2.58),(-.81,2.55),(-1.13,2.29),(-1.36,1.73),(-1.15,2.47),(-.84,2.72),(-.40,2.80)],.08,cyan,c,y=-.10,bevel=.012,edge=pale)
    profile('P06 | ascending lunar fang',[(.10,2.37),(.42,2.37),(.77,2.55),(1.01,2.89),(1.10,3.29),(.88,2.92),(.57,2.77),(.23,2.76),(.08,2.62)],.13,silver,c,bevel=.02,edge=edge)
    profile('P06 | ascending cyan blade',[(.40,2.47),(.75,2.66),(1.10,3.29),(.93,2.72),(.68,2.49),(.43,2.40)],.07,cyan,c,y=-.105,bevel=.009,edge=pale)
    path('P06 | flowing silver staff',[(.04,0,0),(.10,.02,.35),(.03,0,.81),(-.12,0,1.28),(-.10,0,1.81),(.07,0,2.32)],[.065,.08,.07,.065,.082,.10],silver,c,12)
    path('P06 | blue leather grip',[(.10,0,.30),(.07,0,.51),(.03,0,.76),(-.03,0,.99)],[.089,.091,.083,.079],blue,c,12)
    for i in range(6):
        z=.36+i*.10;x=.10-(z-.3)*.18
        line('P06 | grip stitch',[(x-.055,-.08,z),(x+.055,-.08,z+.045)],.008,edge,c)
    profile('P06 | soul open frame',[(-.09,2.16),(-.29,2.45),(-.15,2.84),(-.36,2.51),(-.24,2.22),(0,2.02),(.27,2.23),(.34,2.57),(.18,2.82),(.25,2.48),(.13,2.22)],.10,silver,c,y=-.02,bevel=.015)
    gem('P06 | soul tear',(0,-.15,2.43),.11,.25,.13,[cyan,pale,soul],c,6,7)
    profile('P06 | tapered pommel',[(-.03,.17),(-.11,.02),(.02,-.19),(.15,.02),(.11,.20)],.13,silver,c,bevel=.013,edge=edge)
    for side in [-1,1]:
        line('P06 | flowing filigree',[(side*.12,-.10,1.62),(side*.19,-.10,1.84),(side*.14,-.12,2.07)],.011,edge,c)
    return soul


def magma(c):
    obs=material('P12 | fractured obsidian',(.018,.023,.030),.25,.31)
    edge=material('P12 | cooled fracture edges',(.11,.13,.15),.32,.55)
    steel=material('P12 | scorched forge steel',(.14,.10,.085),.72,.48)
    char=material('P12 | burnt grip',(.045,.026,.020),0,.94)
    lava=material('P12 | lava red',(.82,.065,.008),.02,.35,1.4)
    hot=material('P12 | molten orange',(1,.32,.018),.01,.3,2.0)
    # No crossbar: three offset shells grow around an exposed furnace window.
    profile('P12 | right obsidian claw',[(.16,2.24),(.41,2.19),(.73,2.28),(1.13,1.77),(1.18,2.35),(.99,2.57),(1.06,2.79),(.72,2.72),(.54,3.03),(.27,2.87)],.39,obs,c,bevel=.025,edge=edge)
    profile('P12 | left broken horn',[(-.13,2.18),(-.48,2.27),(-.63,2.38),(-1.14,2.28),(-.90,2.63),(-.69,2.71),(-.55,2.94),(-.27,2.80),(-.17,2.57)],.34,obs,c,y=.04,bevel=.024,edge=edge)
    profile('P12 | upper furnace crown',[(-.31,2.76),(-.44,2.97),(-.18,2.95),(-.11,3.21),(.15,2.99),(.34,3.12),(.36,2.81),(.10,2.71)],.30,obs,c,y=.04,bevel=.023,edge=edge)
    gem('P12 | furnace window',(0,-.09,2.51),.34,.34,.25,[lava,hot],c,12,9)
    for side in [-1,1]:
        path('P12 | forged window guard',[(side*.25,-.23,2.23),(side*.32,-.29,2.49),(side*.20,-.24,2.82)],[.052,.06,.045],steel,c,8)
    line('P12 | right molten fissure',[(.38,-.217,2.73),(.56,-.218,2.58),(.77,-.219,2.62),(.93,-.218,2.40)],.019,hot,c)
    line('P12 | left molten fissure',[(-.24,-.15,2.67),(-.47,-.15,2.53),(-.69,-.15,2.58),(-.89,-.15,2.45)],.018,lava,c)
    path('P12 | reinforced volcanic haft',[(.01,0,0),(-.04,0,.38),(.05,0,.85),(.10,0,1.20),(.03,0,1.76),(0,0,2.36)],[.15,.14,.135,.17,.18,.23],steel,c,10)
    for i in range(6):
        z=.3+i*.16
        ring('P12 | charred grip ridge',(.015,0,z),.157,.035,char,c,major=12)
    for i in range(3):
        z=1.31+i*.23
        profile('P12 | split neck plate',[(-.20,z),(-.24,z+.12),(-.10,z+.27),(.11,z+.25),(.21,z+.08),(.13,z-.02)],.30,obs,c,y=-.015,bevel=.014,edge=edge)
    rock('P12 | lava pommel',(.01,0,.0),(.21,.18,.21),[obs,edge],c,22)
    line('P12 | neck lava conduit',[(.03,-.19,1.33),(-.03,-.18,1.62),(.04,-.19,1.92),(.01,-.20,2.19)],.019,lava,c)
    return hot


def void(c):
    obs=material('P16 | void obsidian',(.022,.016,.045),.35,.22)
    rough=material('P16 | rough dimension scar',(.075,.044,.12),.12,.73)
    silver=material('P16 | cold dimensional silver',(.34,.37,.50),.80,.27)
    violet=material('P16 | saturated void facet',(.22,.035,.46),.1,.22,.25)
    purple=material('P16 | deep purple energy',(.42,.09,.78),.03,.24,1.2)
    # Four separate main pieces with deliberately exposed air between them.
    shapes=[('left anchor',[(-.24,2.39),(-.55,2.41),(-.82,2.65),(-.52,2.96),(-.34,2.79),(-.12,2.65)]),
            ('left floating tooth',[(-.78,2.72),(-1.30,2.39),(-1.08,2.93),(-.71,3.12),(-.62,2.95)]),
            ('right displaced tooth',[(.37,2.50),(.73,2.67),(1.31,3.24),(1.09,2.56),(.83,2.35),(.56,2.36)]),
            ('lower broken prong',[(.30,2.17),(.56,2.21),(.93,1.85),(.80,2.37),(.54,2.44)])]
    for i,(n,p) in enumerate(shapes):profile('P16 | '+n,p,.23 if i%2 else .30,obs,c,y=.03*(i%2),bevel=.016,edge=rough)
    for i,pts in enumerate([[(-.75,.04,2.89),(-.57,.04,2.81),(-.41,.04,2.67)],[(.49,.05,2.50),(.72,.05,2.64),(1.04,.05,2.92)]]):line('P16 | exposed silver armature '+str(i),pts,.035,silver,c)
    for side in [-1,1]:
        line('P16 | open diamond frame',[(0,-.02,2.17),(side*.32,-.02,2.48),(0,-.02,2.83)],.026,silver,c)
    gem('P16 | suspended void prism',(0,-.13,2.50),.145,.26,.18,[violet,purple,obs],c,16,6)
    path('P16 | lower displaced handle',[(.0,0,0),(-.05,0,.28),(-.09,0,.67)],[.105,.12,.095],obs,c,6)
    path('P16 | upper displaced handle',[(.07,.015,.85),(.16,0,1.12),(.10,0,1.57)],[.095,.12,.10],obs,c,6)
    path('P16 | neck fragment',[(-.07,.01,1.77),(-.11,0,2.03),(0,0,2.28)],[.10,.13,.12],obs,c,6)
    line('P16 | lower connector',[(-.08,.04,.59),(-.07,.04,.78),(.10,.04,.93)],.032,silver,c)
    line('P16 | upper connector',[(.12,.04,1.45),(.12,.04,1.67),(-.08,.04,1.88)],.031,silver,c)
    for i,(x,z) in enumerate([(-.03,.29),(.12,1.12),(-.10,2.02)]):
        line('P16 | handle energy incision',[(x-.04,-.11,z-.13),(x+.025,-.11,z+.12)],.012,purple,c)
    profile('P16 | forked pommel',[(-.11,.11),(-.21,-.17),(-.03,-.04),(.12,-.21),(.12,.08)],.16,obs,c,bevel=.012,edge=silver)
    return purple


BUILDERS={'P01':stone,'P05':harvest,'P06':spectral,'P12':magma,'P16':void}


def mist_ribbon(name,points,width,color,c):
    m=material(name+' | translucent preview',color,0,.8,.45)
    m.node_tree.nodes.get('Principled BSDF').inputs['Alpha'].default_value=.09
    verts=[]
    for j,(x,y,z) in enumerate(points):
        taper=math.sin(math.pi*j/(len(points)-1))
        verts.extend([(x,y,z-width*taper),(x,y,z+width*taper)])
    faces=[(j*2,j*2+1,j*2+3,j*2+2) for j in range(len(points)-1)]
    return mesh(name,verts,faces,[m],c)


def aura(pid,c,m):
    rng=random.Random(int(pid[1:])+99)
    if pid=='P01':
        for i in range(7):
            x=-1.04+rng.uniform(-.22,.17);z=2.3+rng.uniform(-.23,.25)
            rock('P01 | impact grain',(x,-.10,z),(.017,.015,.017),m,c,i)
    elif pid=='P05':
        violet=material('P05 | violet smoke trail',(.27,.07,.43),0,.8,.4)
        leaf=material('P05 | aura dry leaf',(.43,.18,.03),0,.8)
        for k in range(2):
            pts=[(-1.15+j*.16,.24+.1*k,2.8+.28*math.sin(j*.43+k)) for j in range(15)]
            line('P05 | violet wisp',pts,.009,violet,c)
            mist_ribbon('P05 | smoke veil',pts,.08,(.27,.07,.43),c)
        for i in range(9):
            x=rng.uniform(-1.4,1.1);z=rng.uniform(1.65,3.3)
            gem('P05 | green ember',(x,.15,z),.018,.03,.01,m,c,i,5)
        profile('P05 | drifting leaf',[(-.9,1.92),(-1.05,2.01),(-1.08,2.18),(-.95,2.13),(-.88,2.01)],.01,leaf,c,y=.20,bevel=0)
    elif pid=='P06':
        for k in range(3):
            pts=[(-1.5+j*.20,.24+.10*k,2.23+k*.11+.15*math.sin(j*.51+k)) for j in range(16)]
            line('P06 | cyan mist filament',pts,.007,m,c)
            mist_ribbon('P06 | low cyan mist',pts,.10,(.08,.45,.58),c)
        for x,z in [(-1.35,2.78),(.92,1.95)]:gem('P06 | orbital soul spark',(x,-.02,z),.035,.065,.035,m,c,4,6)
    elif pid=='P12':
        for i in range(18):
            x=rng.uniform(-1.1,1.1);z=rng.uniform(2.0,3.67)
            gem('P12 | ascending ember',(x,.10,z),.014,.035,.012,m,c,i,5)
        for k in range(2):
            pts=[(-.6+k*.9+.08*math.sin(j*.8),.23,2.6+j*.11) for j in range(10)]
            line('P12 | heat shimmer',pts,.006,m,c)
    else:
        for i,(x,z) in enumerate([(-1.38,3.08),(.95,3.45),(-.65,1.98),(.51,1.69)]):
            profile('P16 | orbital dimension triangle',[(x,z),(x+.12,z+.20),(x+.21,z-.035)],.025,m,c,y=.16,bevel=.005)
        for start in [0.15,1.9,3.9]:
            pts=[(1.38*math.cos(start+j*.10),.28,2.55+.65*math.sin(start+j*.10)) for j in range(9)]
            line('P16 | interrupted pulse arc',pts,.009,m,c)


def build(pid):
    reset();master=collection('01 MASTER | unique sculpt');ac=collection('03 AURA_PREVIEW | not gameplay')
    glow=BUILDERS[pid](master);aura(pid,ac,glow)
    apply_origins(master,(0,0,-.65));apply_origins(ac,(0,0,-.65));ac.hide_render=True
    for o in ac.objects:o.hide_set(True)
    game=clone_game(master)
    target=(0,0,.95);st,cam=studio(target,4.7)
    stem=f'BH_PICK_{pid}_{NAMES[pid]}_V02'
    bpy.ops.wm.save_as_mainfile(filepath=str(ROOT/'models'/f'{stem}.blend'))
    export(game,stem)
    render(cam,target,(0,-7,.95),ROOT/'renders'/f'{stem}_Front.png')
    render(cam,target,(3.0,-7,2.1),ROOT/'renders'/f'{stem}_Iso.png')
    ac.hide_render=False
    scene=bpy.context.scene;scene.use_nodes=True
    nodes=scene.node_tree.nodes;nodes.clear()
    layer=nodes.new('CompositorNodeRLayers');glare=nodes.new('CompositorNodeGlare');glare.glare_type='FOG_GLOW';glare.quality='HIGH';glare.threshold=.9;glare.size=7;glare.mix=-.75
    output=nodes.new('CompositorNodeComposite');scene.node_tree.links.new(layer.outputs['Image'],glare.inputs['Image']);scene.node_tree.links.new(glare.outputs['Image'],output.inputs['Image'])
    world=bpy.context.scene.world.node_tree.nodes['Background'];world.inputs['Color'].default_value=(.006,.009,.018,1);world.inputs['Strength'].default_value=.17
    render(cam,target,(1.1,-7,1.45),ROOT/'renders'/f'{stem}_Dark.png')
    out={'id':pid,'stem':stem,'master':stats(master),'game':stats(game),'aura_meshes':len(ac.objects),'origin':'grip reference; applied transforms'}
    (ROOT/'docs'/f'{pid}_V02_Technical.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PILOT_OK',pid,out['game'],flush=True)

if __name__=='__main__':
    args=sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else []
    ids=list(BUILDERS) if args==['--all'] else [args[1]] if len(args)==2 and args[0]=='--id' else []
    if not ids:raise SystemExit('Use -- --all or -- --id P01')
    for pid in ids:build(pid)
