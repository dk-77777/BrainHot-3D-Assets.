"""Write the review report and a dependency-free local HTML gallery from V02 evidence."""
import json,html
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
IDS=['P01','P05','P06','P12','P16']
LABELS={'P01':'Picareta Rúnica de Pedra','P05':'Colheita Sombria','P06':'Presa Espectral','P12':'Picareta de Magma Profano','P16':'Fragmento Void'}
DISTINCT={
'P01':'Cabeça compacta de ardósia lascada; cabo grosso de castanho; amarração em X e runa pequena. É o único piloto sem grande núcleo gemado e sem aura passiva.',
'P05':'Garras de colheita de comprimentos diferentes; haste de raiz entrelaçada com espinhos; coração âmbar preso por cinco costelas de abóbora. Folhas e vinhas definem o tema.',
'P06':'Duas presas em S e encaixe aberto; haste fina com curva contínua, couro azul e pommel pontiagudo. Joia de alma suspensa na moldura e filigranas de prata.',
'P12':'Três placas irregulares de obsidiana compõem uma cabeça assimétrica; janela de lava protegida; cabo espesso com placas vulcânicas e grip queimado. Não usa barra transversal comum.',
'P16':'Dentes deslocados com intervalos de ar; armação angular visível e prisma púrpura. Cabo em três seções desalinhadas e conectores expostos; pommel bifurcado.'}
ORE_NOTES=[
'Basalto escuro em camadas, ledges incorporados e fissuras finas azuladas.',
'Quartzo de seis faces preservado, contraste com rocha neutra e pontas menores.',
'Ametista com facetas mais consistentes, pequenos cristais secundários e núcleo moderado.',
'Resina âmbar preservada, luzes controladas, nódulos menores e rocha mais escura.',
'Conjunto de seis placas preservado, runas bifurcadas e contraste de pedra/inlay.',
'Agrupamento em X preservado, pontas afinadas e brotos menores entre os volumes.',
'Boulder lunar refinado a partir do volume original, quatro crateras rasas reais e tons claros foscos sem emissão ampla.',
'Colunas espectrais mantidas, pequenos cristais junto aos encaixes e base grafite.',
'Gemas azuis com faixas de reflexão mais coerentes e assento rochoso escuro.',
'Gelo com pontas refinadas, cristais menores e leitura ciano contra ardósia.',
'Aro e disco preservados; relevo mineral, contraste roxo/grafite e escala intermediária.',
'Base preservada; o coração virou uma única gema angular apoiada em dois relevos de basalto.',
'Ferro e cinzas com rocha escura, sulcos projetados na superfície e brilho quente localizado.',
'Espigas de brasa com diferenças de tamanho, brotos pequenos e rocha mais escura.',
'Lâminas rituais preservadas, acabamento de obsidiana e inscrições contidas.',
'Cristais rubros com pontas estreitas, secundários menores e fissuras controladas.',
'Anel de obsidiana e gema quadrada preservados, contraste e relevo no leito.',
'Escória irregular com camadas rochosas e brilho restrito a veios/cristais.',
'Fragmentos escalonados preservados; quinas e separação material de rocha/void.',
'Prisma central enriquecido por brotos menores, contraste ciano/violeta e encaixes.',
'Monólito preto preservado, fendas estreitas e facetas de rugosidade contrastante.',
'Prisma herói preservado; pequenos periféricos e graduação de facetas saturadas.',
'Eixos cruzados e aro mantidos; pedra mais estruturada e energia contida.',
'Prisma assimétrico enriquecido com pequenos cristais e cinco ressaltos de estrela integrados à base.'
]
picks=[json.loads((ROOT/'docs'/f'{i}_V02_Technical.json').read_text()) for i in IDS]
ores=[json.loads((ROOT/'docs'/f'O{i:02}_V02_Technical.json').read_text()) for i in range(1,25)]
validation=json.loads((ROOT/'docs/Art_V02_Validation.json').read_text())
assert validation['passed']==29 and not validation['errors'],'Validate all V02 artifacts before writing review'
sil=json.loads((ROOT/'docs/Pickaxe_V02_Silhouette_Review.json').read_text())
lines=['# Revisão de arte V02 — BrainHot Mining','',
'Escopo: cinco picaretas redesenhadas individualmente e 24 minérios refinados a partir das malhas V01. Todos os arquivos V01 foram preservados. A produção das outras 23 picaretas permanece suspensa até aprovação destes cinco pilotos.','',
'## Cinco projetos próprios','',
'[Direção registrada antes da modelagem](Pickaxe_Pilots_V02_Design.md) · [Galeria local](Art_Review_V02.html) · [Especificações das auras](../data/Pickaxe_V02_Aura_Specs.json)','',
'![Comparação dos cinco pilotos](../renders/Pickaxe_Pilots_V02_Lineup.png)','',
'![Comparação sem cor, material ou aura](../renders/Pickaxe_Pilots_V02_Silhouettes.png)','',
f'A prancha de silhuetas foi inspecionada visualmente. A maior interseção/união entre máscaras frontais de dois pilotos na mesma escala foi {sil["max_overlap"]*100:.2f}%. Essa medida é um apoio, não um limiar oficial de aprovação artística. Os contornos, vãos, distribuição de massa e cabos são diferentes.','']
for p in picks:
 pid=p['id'];stem=p['stem']
 lines += [f'### {pid} — {LABELS[pid]}','',DISTINCT[pid],'',
 f'GAME: **{p["game"]["triangles"]:,} triângulos**, {p["game"]["meshes"]} malhas. [.blend](../models/{stem}.blend) · [GLB](../exports/{stem}.glb)','',
 '| Frontal | Isométrico | Fundo escuro / aura |','| --- | --- | --- |',
 f'| ![](../renders/{stem}_Front.png) | ![](../renders/{stem}_Iso.png) | ![](../renders/{stem}_Dark.png) |','']
lines += ['As auras são prévias estáticas em coleção separada: grãos de impacto, folhas/brasas, fitas de névoa, faíscas vulcânicas e triângulos dimensionais. O GLB principal exclui essas coleções. O JSON descreve eventos e parâmetros para uma implementação futura no Roblox; não contém ParticleEmitters já integrados ao jogo.','',
'## Minérios: refinamento e escala','',
'[O01–O06](../renders/Ores_V02_Board_1.png) · [O07–O12](../renders/Ores_V02_Board_2.png) · [O13–O18](../renders/Ores_V02_Board_3.png) · [O19–O24](../renders/Ores_V02_Board_4.png)','',
'A progressão conceitual vai de +12% a +23% nos três eixos. Os novos elementos foram ajustados ao envelope original antes de aplicar a escala indicada, evitando aumentar o asset além do intervalo pedido. Isso não atribui raridade funcional aos IDs do jogo. Rocha e cristais têm cores e roughness separadas; a emissão é localizada em núcleos e inlays. Os sulcos novos são linhas projetadas na superfície por raycast, não booleanos de colisão.','',
'Nas comparações, V01 fica à esquerda e V02 à direita, sob a mesma câmera, iluminação e unidade de cena. As duas versões são renderizadas juntas; não foi ampliada uma imagem pronta.','',
'| ID | Minério | Escala | Triângulos GAME: antes → depois | Comparação e arquivos |','| --- | --- | ---: | ---: | --- |']
for o in ores:
 stem=o['stem'];pid=o['id'];note=ORE_NOTES[int(pid[1:])-1]
 lines.append(f'| {pid} | {o["name"]} | +{(o["nominal_scale"]-1)*100:.2f}% | {o["before_game"]["triangles"]} → {o["after_game"]["triangles"]} | [Antes/depois](../renders/{stem}_Before_After.png) · [Iso](../renders/{stem}_Iso.png) · [.blend](../models/{stem}.blend) · [GLB](../exports/{stem}.glb) |')
lines += ['', '### Justificativa por minério', '']
for o in ores:lines.append(f'- **{o["id"]} — {o["name"]}:** {ORE_NOTES[int(o["id"][1:])-1]}')
lines += ['', '## Evidência técnica e limites', '',
f'- {validation["passed"]}/{validation["expected"]} modelos V02 reabertos e GLBs reimportados com a mesma contagem de triângulos e malhas. Transformações identidade, coordenadas finitas, sem arestas abertas/não manifold ou faces de área zero nas malhas GAME verificadas.',
'- 15 renders de picaretas e 72 renders de minérios em 1024 × 1024; 24 comparações em 1536 × 1024; pranchas de pilotos em 2560 × 1024. A aprovação artística continua pendente.',
'- Os modelos preservam pivô comum. Picaretas usam referência de pega na origem; minérios usam referência de base. A escala em studs, colisores, normalização de importação, soldas dos fragmentos da Void e desempenho mobile ainda precisam de teste no Roblox Studio.',
'- Não foi modificado o projeto Roblox. Texturas/atlas, VFX runtime, colisão no Studio e testes de gameplay não foram produzidos nesta etapa. O uso de Principled PBR evita nós procedurais exclusivos, mas a aparência da emissão no importador precisa ser conferida.',
'- A aura e os fragmentos orbitais de prévia não devem virar colisores físicos independentes. A implementação deve usar efeitos visuais de evento, com variante de movimento reduzido.',
'- O Blender Debian não oferece OpenImageDenoise; as imagens usam Cycles sem denoiser. Ainda pode haver ruído fino em áreas de sombra, sobretudo nas comparações.',
'- Detalhes de sulcos e filigranas são geometrias pequenas. Precisam ser avaliados na distância real de câmera; podem ser omitidos de LODs distantes.',
'', '[Dados completos de validação](Art_V02_Validation.json) · [Dados de silhueta](Pickaxe_V02_Silhouette_Review.json)', '',
'## Reconstrução', '', '```sh',
'mkdir -p /tmp/blender-xdg/config /tmp/blender-xdg/cache',
'XDG_CONFIG_HOME=/tmp/blender-xdg/config XDG_CACHE_HOME=/tmp/blender-xdg/cache blender -b -t 5 --python-exit-code 1 --python scripts/build_pickaxe_pilots_v02.py -- --all',
'XDG_CONFIG_HOME=/tmp/blender-xdg/config XDG_CACHE_HOME=/tmp/blender-xdg/cache blender -b -t 5 --python-exit-code 1 --python scripts/review_pickaxe_silhouettes_v02.py',
'XDG_CONFIG_HOME=/tmp/blender-xdg/config XDG_CACHE_HOME=/tmp/blender-xdg/cache blender -b -t 5 --python-exit-code 1 --python scripts/refine_ores_v02.py -- --all',
'XDG_CONFIG_HOME=/tmp/blender-xdg/config XDG_CACHE_HOME=/tmp/blender-xdg/cache blender -b -t 5 --python-exit-code 1 --python scripts/review_ores_v02.py',
'XDG_CONFIG_HOME=/tmp/blender-xdg/config XDG_CACHE_HOME=/tmp/blender-xdg/cache blender -b -t 2 --python-exit-code 1 --python scripts/finalize_art_v02.py',
'XDG_CONFIG_HOME=/tmp/blender-xdg/config XDG_CACHE_HOME=/tmp/blender-xdg/cache blender -b -t 2 --python-exit-code 1 --python scripts/validate_art_v02.py',
'python3 scripts/write_art_v02_review.py','```','']
(ROOT/'docs/Art_Direction_V02_Report.md').write_text('\n'.join(lines))
status={'revision':'V02','artistic_approval':'pending user review','roblox_integration':'not performed','v01_pickaxes':'rejected art direction; preserved as reference','pilot_ids':IDS,'blocked_other_pickaxes':[f'P{i:02}' for i in range(1,29) if f'P{i:02}' not in IDS],'ore_revision_ids':[f'O{i:02}' for i in range(1,25)]}
(ROOT/'docs/ASSET_STATUS_V02.json').write_text(json.dumps(status,ensure_ascii=False,indent=2)+'\n')
# A local gallery: all media remain relative files, no external scripts or network.
items=[]
for p in picks:items.append({'id':p['id'],'name':LABELS[p['id']],'kind':'Picareta','stem':p['stem'],'text':DISTINCT[p['id']],'triangles':p['game']['triangles'],'views':['Front','Iso','Dark']})
for o in ores:items.append({'id':o['id'],'name':o['name'],'kind':'Minério','stem':o['stem'],'text':ORE_NOTES[int(o['id'][1:])-1], 'triangles':o['after_game']['triangles'],'scale':round((o['nominal_scale']-1)*100,2),'views':['Before_After','Front','Iso','Back']})
page='''<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>BrainHot — revisão V02</title><style>
body{margin:0;background:#10141e;color:#e6e8f0;font:16px system-ui}header{padding:28px 5vw;border-bottom:1px solid #343b51}h1{margin:0 0 8px;font-size:28px}p{line-height:1.55}main{display:grid;grid-template-columns:280px 1fr;gap:24px;padding:24px 5vw}nav{max-height:76vh;overflow:auto}button{display:block;width:100%;text-align:left;margin:4px 0;padding:12px;border:1px solid #343b51;border-radius:8px;background:#1b2233;color:inherit;cursor:pointer}button.active{border-color:#ab90ff;background:#33294c}#views{display:flex;gap:8px}#views button{width:auto}img{width:100%;max-height:70vh;object-fit:contain;background:#080b12;border-radius:12px}a{color:#cbb9ff}small{color:#b2bbd0}@media(max-width:760px){main{grid-template-columns:1fr}nav{max-height:200px}}</style>
<header><h1>BrainHot Mining · revisão V02</h1><small>Cinco pilotos com estruturas próprias · 24 minérios refinados · aprovação artística pendente</small></header><main><nav id="nav"></nav><section><h2 id="title"></h2><p id="text"></p><p id="stats"></p><div id="views"></div><img id="image"><p id="files"></p></section></main><script>
const items=DATA;const labels={Front:'Frente',Iso:'Isométrico',Dark:'Escuro / aura',Back:'Traseira',Before_After:'Antes → depois'};let selected=0;
function show(i){selected=i;let a=items[i];document.querySelectorAll('#nav button').forEach((b,n)=>b.classList.toggle('active',n===i));document.getElementById('title').textContent=a.id+' · '+a.name;document.getElementById('text').textContent=a.text;document.getElementById('stats').textContent=a.triangles.toLocaleString('pt-BR')+' triângulos GAME'+(a.scale?' · escala +'+a.scale+'%':'');let views=document.getElementById('views');views.replaceChildren();a.views.forEach(v=>{let b=document.createElement('button');b.textContent=labels[v];b.onclick=()=>{document.getElementById('image').src='../renders/'+a.stem+'_'+v+'.png';document.getElementById('image').alt=a.name+' — '+labels[v]};views.append(b)});views.firstChild.click();let f=document.getElementById('files');f.replaceChildren();[['Modelo Blender','models','.blend'],['GLB','exports','.glb']].forEach(([label,dir,ext])=>{let link=document.createElement('a');link.href='../'+dir+'/'+a.stem+ext;link.textContent=label;link.style.marginRight='20px';f.append(link)})}
items.forEach((a,i)=>{let b=document.createElement('button');b.textContent=a.id+' · '+a.name;b.onclick=()=>show(i);document.getElementById('nav').append(b)});show(0);
</script></html>'''.replace('DATA',json.dumps(items,ensure_ascii=False))
(ROOT/'docs/Art_Review_V02.html').write_text(page)
print('REVIEW_WRITTEN',len(items))
