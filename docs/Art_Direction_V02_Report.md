# Revisão de arte V02 — BrainHot Mining

Escopo: cinco picaretas redesenhadas individualmente e 24 minérios refinados a partir das malhas V01. Todos os arquivos V01 foram preservados. A produção das outras 23 picaretas permanece suspensa até aprovação destes cinco pilotos.

## Cinco projetos próprios

[Direção registrada antes da modelagem](Pickaxe_Pilots_V02_Design.md) · [Galeria local](Art_Review_V02.html) · [Especificações das auras](../data/Pickaxe_V02_Aura_Specs.json)

![Comparação dos cinco pilotos](../renders/Pickaxe_Pilots_V02_Lineup.png)

![Comparação sem cor, material ou aura](../renders/Pickaxe_Pilots_V02_Silhouettes.png)

A prancha de silhuetas foi inspecionada visualmente. A maior interseção/união entre máscaras frontais de dois pilotos na mesma escala foi 47.55%. Essa medida é um apoio, não um limiar oficial de aprovação artística. Os contornos, vãos, distribuição de massa e cabos são diferentes.

### P01 — Picareta Rúnica de Pedra

Cabeça compacta de ardósia lascada; cabo grosso de castanho; amarração em X e runa pequena. É o único piloto sem grande núcleo gemado e sem aura passiva.

GAME: **2,120 triângulos**, 19 malhas. [.blend](../models/BH_PICK_P01_Picareta_Runica_de_Pedra_V02.blend) · [GLB](../exports/BH_PICK_P01_Picareta_Runica_de_Pedra_V02.glb)

| Frontal | Isométrico | Fundo escuro / aura |
| --- | --- | --- |
| ![](../renders/BH_PICK_P01_Picareta_Runica_de_Pedra_V02_Front.png) | ![](../renders/BH_PICK_P01_Picareta_Runica_de_Pedra_V02_Iso.png) | ![](../renders/BH_PICK_P01_Picareta_Runica_de_Pedra_V02_Dark.png) |

### P05 — Colheita Sombria

Garras de colheita de comprimentos diferentes; haste de raiz entrelaçada com espinhos; coração âmbar preso por cinco costelas de abóbora. Folhas e vinhas definem o tema.

GAME: **1,912 triângulos**, 20 malhas. [.blend](../models/BH_PICK_P05_Colheita_Sombria_V02.blend) · [GLB](../exports/BH_PICK_P05_Colheita_Sombria_V02.glb)

| Frontal | Isométrico | Fundo escuro / aura |
| --- | --- | --- |
| ![](../renders/BH_PICK_P05_Colheita_Sombria_V02_Front.png) | ![](../renders/BH_PICK_P05_Colheita_Sombria_V02_Iso.png) | ![](../renders/BH_PICK_P05_Colheita_Sombria_V02_Dark.png) |

### P06 — Presa Espectral

Duas presas em S e encaixe aberto; haste fina com curva contínua, couro azul e pommel pontiagudo. Joia de alma suspensa na moldura e filigranas de prata.

GAME: **1,554 triângulos**, 17 malhas. [.blend](../models/BH_PICK_P06_Presa_Espectral_V02.blend) · [GLB](../exports/BH_PICK_P06_Presa_Espectral_V02.glb)

| Frontal | Isométrico | Fundo escuro / aura |
| --- | --- | --- |
| ![](../renders/BH_PICK_P06_Presa_Espectral_V02_Front.png) | ![](../renders/BH_PICK_P06_Presa_Espectral_V02_Iso.png) | ![](../renders/BH_PICK_P06_Presa_Espectral_V02_Dark.png) |

### P12 — Picareta de Magma Profano

Três placas irregulares de obsidiana compõem uma cabeça assimétrica; janela de lava protegida; cabo espesso com placas vulcânicas e grip queimado. Não usa barra transversal comum.

GAME: **2,442 triângulos**, 20 malhas. [.blend](../models/BH_PICK_P12_Picareta_de_Magma_Profano_V02.blend) · [GLB](../exports/BH_PICK_P12_Picareta_de_Magma_Profano_V02.glb)

| Frontal | Isométrico | Fundo escuro / aura |
| --- | --- | --- |
| ![](../renders/BH_PICK_P12_Picareta_de_Magma_Profano_V02_Front.png) | ![](../renders/BH_PICK_P12_Picareta_de_Magma_Profano_V02_Iso.png) | ![](../renders/BH_PICK_P12_Picareta_de_Magma_Profano_V02_Dark.png) |

### P16 — Fragmento Void

Dentes deslocados com intervalos de ar; armação angular visível e prisma púrpura. Cabo em três seções desalinhadas e conectores expostos; pommel bifurcado.

GAME: **1,068 triângulos**, 18 malhas. [.blend](../models/BH_PICK_P16_Fragmento_Void_V02.blend) · [GLB](../exports/BH_PICK_P16_Fragmento_Void_V02.glb)

| Frontal | Isométrico | Fundo escuro / aura |
| --- | --- | --- |
| ![](../renders/BH_PICK_P16_Fragmento_Void_V02_Front.png) | ![](../renders/BH_PICK_P16_Fragmento_Void_V02_Iso.png) | ![](../renders/BH_PICK_P16_Fragmento_Void_V02_Dark.png) |

As auras são prévias estáticas em coleção separada: grãos de impacto, folhas/brasas, fitas de névoa, faíscas vulcânicas e triângulos dimensionais. O GLB principal exclui essas coleções. O JSON descreve eventos e parâmetros para uma implementação futura no Roblox; não contém ParticleEmitters já integrados ao jogo.

## Minérios: refinamento e escala

[O01–O06](../renders/Ores_V02_Board_1.png) · [O07–O12](../renders/Ores_V02_Board_2.png) · [O13–O18](../renders/Ores_V02_Board_3.png) · [O19–O24](../renders/Ores_V02_Board_4.png)

A progressão conceitual vai de +12% a +23% nos três eixos. Os novos elementos foram ajustados ao envelope original antes de aplicar a escala indicada, evitando aumentar o asset além do intervalo pedido. Isso não atribui raridade funcional aos IDs do jogo. Rocha e cristais têm cores e roughness separadas; a emissão é localizada em núcleos e inlays. Os sulcos novos são linhas projetadas na superfície por raycast, não booleanos de colisão.

Nas comparações, V01 fica à esquerda e V02 à direita, sob a mesma câmera, iluminação e unidade de cena. As duas versões são renderizadas juntas; não foi ampliada uma imagem pronta.

| ID | Minério | Escala | Triângulos GAME: antes → depois | Comparação e arquivos |
| --- | --- | ---: | ---: | --- |
| O01 | Pedra Brumosa | +12.00% | 852 → 2452 | [Antes/depois](../renders/BH_ORE_O01_Pedra_Brumosa_V02_Before_After.png) · [Iso](../renders/BH_ORE_O01_Pedra_Brumosa_V02_Iso.png) · [.blend](../models/BH_ORE_O01_Pedra_Brumosa_V02.blend) · [GLB](../exports/BH_ORE_O01_Pedra_Brumosa_V02.glb) |
| O02 | Quartzo de Abóbora | +12.48% | 352 → 1234 | [Antes/depois](../renders/BH_ORE_O02_Quartzo_de_Abobora_V02_Before_After.png) · [Iso](../renders/BH_ORE_O02_Quartzo_de_Abobora_V02_Iso.png) · [.blend](../models/BH_ORE_O02_Quartzo_de_Abobora_V02.blend) · [GLB](../exports/BH_ORE_O02_Quartzo_de_Abobora_V02.glb) |
| O03 | Cristal Crepuscular | +12.96% | 836 → 2300 | [Antes/depois](../renders/BH_ORE_O03_Cristal_Crepuscular_V02_Before_After.png) · [Iso](../renders/BH_ORE_O03_Cristal_Crepuscular_V02_Iso.png) · [.blend](../models/BH_ORE_O03_Cristal_Crepuscular_V02.blend) · [GLB](../exports/BH_ORE_O03_Cristal_Crepuscular_V02.glb) |
| O04 | Âmbar Espiritual | +13.43% | 692 → 2078 | [Antes/depois](../renders/BH_ORE_O04_Ambar_Espiritual_V02_Before_After.png) · [Iso](../renders/BH_ORE_O04_Ambar_Espiritual_V02_Iso.png) · [.blend](../models/BH_ORE_O04_Ambar_Espiritual_V02.blend) · [GLB](../exports/BH_ORE_O04_Ambar_Espiritual_V02.glb) |
| O05 | Rocha das Runas | +13.91% | 468 → 1240 | [Antes/depois](../renders/BH_ORE_O05_Rocha_das_Runas_V02_Before_After.png) · [Iso](../renders/BH_ORE_O05_Rocha_das_Runas_V02_Iso.png) · [.blend](../models/BH_ORE_O05_Rocha_das_Runas_V02.blend) · [GLB](../exports/BH_ORE_O05_Rocha_das_Runas_V02.glb) |
| O06 | Ametista de Colheita | +14.39% | 416 → 1344 | [Antes/depois](../renders/BH_ORE_O06_Ametista_de_Colheita_V02_Before_After.png) · [Iso](../renders/BH_ORE_O06_Ametista_de_Colheita_V02_Iso.png) · [.blend](../models/BH_ORE_O06_Ametista_de_Colheita_V02.blend) · [GLB](../exports/BH_ORE_O06_Ametista_de_Colheita_V02.glb) |
| O07 | Pedra Lunar | +14.87% | 732 → 1824 | [Antes/depois](../renders/BH_ORE_O07_Pedra_Lunar_V02_Before_After.png) · [Iso](../renders/BH_ORE_O07_Pedra_Lunar_V02_Iso.png) · [.blend](../models/BH_ORE_O07_Pedra_Lunar_V02.blend) · [GLB](../exports/BH_ORE_O07_Pedra_Lunar_V02.glb) |
| O08 | Quartzo Espectral | +15.35% | 460 → 1592 | [Antes/depois](../renders/BH_ORE_O08_Quartzo_Espectral_V02_Before_After.png) · [Iso](../renders/BH_ORE_O08_Quartzo_Espectral_V02_Iso.png) · [.blend](../models/BH_ORE_O08_Quartzo_Espectral_V02.blend) · [GLB](../exports/BH_ORE_O08_Quartzo_Espectral_V02.glb) |
| O09 | Safira Sepulcral | +15.83% | 740 → 2310 | [Antes/depois](../renders/BH_ORE_O09_Safira_Sepulcral_V02_Before_After.png) · [Iso](../renders/BH_ORE_O09_Safira_Sepulcral_V02_Iso.png) · [.blend](../models/BH_ORE_O09_Safira_Sepulcral_V02.blend) · [GLB](../exports/BH_ORE_O09_Safira_Sepulcral_V02.glb) |
| O10 | Gelo Fantasma | +16.30% | 540 → 1862 | [Antes/depois](../renders/BH_ORE_O10_Gelo_Fantasma_V02_Before_After.png) · [Iso](../renders/BH_ORE_O10_Gelo_Fantasma_V02_Iso.png) · [.blend](../models/BH_ORE_O10_Gelo_Fantasma_V02.blend) · [GLB](../exports/BH_ORE_O10_Gelo_Fantasma_V02.glb) |
| O11 | Eclipse Enjaulado | +16.78% | 596 → 1314 | [Antes/depois](../renders/BH_ORE_O11_Eclipse_Enjaulado_V02_Before_After.png) · [Iso](../renders/BH_ORE_O11_Eclipse_Enjaulado_V02_Iso.png) · [.blend](../models/BH_ORE_O11_Eclipse_Enjaulado_V02.blend) · [GLB](../exports/BH_ORE_O11_Eclipse_Enjaulado_V02.glb) |
| O12 | Coração Lanternado | +17.26% | 484 → 958 | [Antes/depois](../renders/BH_ORE_O12_Coracao_Lanternado_V02_Before_After.png) · [Iso](../renders/BH_ORE_O12_Coracao_Lanternado_V02_Iso.png) · [.blend](../models/BH_ORE_O12_Coracao_Lanternado_V02.blend) · [GLB](../exports/BH_ORE_O12_Coracao_Lanternado_V02.glb) |
| O13 | Ferro das Cinzas | +17.74% | 852 → 2556 | [Antes/depois](../renders/BH_ORE_O13_Ferro_das_Cinzas_V02_Before_After.png) · [Iso](../renders/BH_ORE_O13_Ferro_das_Cinzas_V02_Iso.png) · [.blend](../models/BH_ORE_O13_Ferro_das_Cinzas_V02.blend) · [GLB](../exports/BH_ORE_O13_Ferro_das_Cinzas_V02.glb) |
| O14 | Cristal de Brasa | +18.22% | 756 → 2698 | [Antes/depois](../renders/BH_ORE_O14_Cristal_de_Brasa_V02_Before_After.png) · [Iso](../renders/BH_ORE_O14_Cristal_de_Brasa_V02_Iso.png) · [.blend](../models/BH_ORE_O14_Cristal_de_Brasa_V02.blend) · [GLB](../exports/BH_ORE_O14_Cristal_de_Brasa_V02.glb) |
| O15 | Obsidiana Ritual | +18.70% | 456 → 1796 | [Antes/depois](../renders/BH_ORE_O15_Obsidiana_Ritual_V02_Before_After.png) · [Iso](../renders/BH_ORE_O15_Obsidiana_Ritual_V02_Iso.png) · [.blend](../models/BH_ORE_O15_Obsidiana_Ritual_V02.blend) · [GLB](../exports/BH_ORE_O15_Obsidiana_Ritual_V02.glb) |
| O16 | Rubi de Magma | +19.17% | 624 → 2308 | [Antes/depois](../renders/BH_ORE_O16_Rubi_de_Magma_V02_Before_After.png) · [Iso](../renders/BH_ORE_O16_Rubi_de_Magma_V02_Iso.png) · [.blend](../models/BH_ORE_O16_Rubi_de_Magma_V02.blend) · [GLB](../exports/BH_ORE_O16_Rubi_de_Magma_V02.glb) |
| O17 | Núcleo Infernal | +19.65% | 468 → 1292 | [Antes/depois](../renders/BH_ORE_O17_Nucleo_Infernal_V02_Before_After.png) · [Iso](../renders/BH_ORE_O17_Nucleo_Infernal_V02_Iso.png) · [.blend](../models/BH_ORE_O17_Nucleo_Infernal_V02.blend) · [GLB](../exports/BH_ORE_O17_Nucleo_Infernal_V02.glb) |
| O18 | Escória Demoníaca | +20.13% | 984 → 2864 | [Antes/depois](../renders/BH_ORE_O18_Escoria_Demoniaca_V02_Before_After.png) · [Iso](../renders/BH_ORE_O18_Escoria_Demoniaca_V02_Iso.png) · [.blend](../models/BH_ORE_O18_Escoria_Demoniaca_V02.blend) · [GLB](../exports/BH_ORE_O18_Escoria_Demoniaca_V02.glb) |
| O19 | Fragmento Vazio | +20.61% | 320 → 1332 | [Antes/depois](../renders/BH_ORE_O19_Fragmento_Vazio_V02_Before_After.png) · [Iso](../renders/BH_ORE_O19_Fragmento_Vazio_V02_Iso.png) · [.blend](../models/BH_ORE_O19_Fragmento_Vazio_V02.blend) · [GLB](../exports/BH_ORE_O19_Fragmento_Vazio_V02.glb) |
| O20 | Cristal Anômalo | +21.09% | 364 → 1626 | [Antes/depois](../renders/BH_ORE_O20_Cristal_Anomalo_V02_Before_After.png) · [Iso](../renders/BH_ORE_O20_Cristal_Anomalo_V02_Iso.png) · [.blend](../models/BH_ORE_O20_Cristal_Anomalo_V02.blend) · [GLB](../exports/BH_ORE_O20_Cristal_Anomalo_V02.glb) |
| O21 | Nullstone | +21.57% | 320 → 1226 | [Antes/depois](../renders/BH_ORE_O21_Nullstone_V02_Before_After.png) · [Iso](../renders/BH_ORE_O21_Nullstone_V02_Iso.png) · [.blend](../models/BH_ORE_O21_Nullstone_V02.blend) · [GLB](../exports/BH_ORE_O21_Nullstone_V02.glb) |
| O22 | Prisma Galáctico | +22.04% | 548 → 2086 | [Antes/depois](../renders/BH_ORE_O22_Prisma_Galactico_V02_Before_After.png) · [Iso](../renders/BH_ORE_O22_Prisma_Galactico_V02_Iso.png) · [.blend](../models/BH_ORE_O22_Prisma_Galactico_V02.blend) · [GLB](../exports/BH_ORE_O22_Prisma_Galactico_V02.glb) |
| O23 | Singularidade Lapidada | +22.52% | 480 → 1354 | [Antes/depois](../renders/BH_ORE_O23_Singularidade_Lapidada_V02_Before_After.png) · [Iso](../renders/BH_ORE_O23_Singularidade_Lapidada_V02_Iso.png) · [.blend](../models/BH_ORE_O23_Singularidade_Lapidada_V02.blend) · [GLB](../exports/BH_ORE_O23_Singularidade_Lapidada_V02.glb) |
| O24 | Coração do Horizonte | +23.00% | 592 → 2304 | [Antes/depois](../renders/BH_ORE_O24_Coracao_do_Horizonte_V02_Before_After.png) · [Iso](../renders/BH_ORE_O24_Coracao_do_Horizonte_V02_Iso.png) · [.blend](../models/BH_ORE_O24_Coracao_do_Horizonte_V02.blend) · [GLB](../exports/BH_ORE_O24_Coracao_do_Horizonte_V02.glb) |

### Justificativa por minério

- **O01 — Pedra Brumosa:** Basalto escuro em camadas, ledges incorporados e fissuras finas azuladas.
- **O02 — Quartzo de Abóbora:** Quartzo de seis faces preservado, contraste com rocha neutra e pontas menores.
- **O03 — Cristal Crepuscular:** Ametista com facetas mais consistentes, pequenos cristais secundários e núcleo moderado.
- **O04 — Âmbar Espiritual:** Resina âmbar preservada, luzes controladas, nódulos menores e rocha mais escura.
- **O05 — Rocha das Runas:** Conjunto de seis placas preservado, runas bifurcadas e contraste de pedra/inlay.
- **O06 — Ametista de Colheita:** Agrupamento em X preservado, pontas afinadas e brotos menores entre os volumes.
- **O07 — Pedra Lunar:** Boulder lunar refinado a partir do volume original, quatro crateras rasas reais e tons claros foscos sem emissão ampla.
- **O08 — Quartzo Espectral:** Colunas espectrais mantidas, pequenos cristais junto aos encaixes e base grafite.
- **O09 — Safira Sepulcral:** Gemas azuis com faixas de reflexão mais coerentes e assento rochoso escuro.
- **O10 — Gelo Fantasma:** Gelo com pontas refinadas, cristais menores e leitura ciano contra ardósia.
- **O11 — Eclipse Enjaulado:** Aro e disco preservados; relevo mineral, contraste roxo/grafite e escala intermediária.
- **O12 — Coração Lanternado:** Base preservada; o coração virou uma única gema angular apoiada em dois relevos de basalto.
- **O13 — Ferro das Cinzas:** Ferro e cinzas com rocha escura, sulcos projetados na superfície e brilho quente localizado.
- **O14 — Cristal de Brasa:** Espigas de brasa com diferenças de tamanho, brotos pequenos e rocha mais escura.
- **O15 — Obsidiana Ritual:** Lâminas rituais preservadas, acabamento de obsidiana e inscrições contidas.
- **O16 — Rubi de Magma:** Cristais rubros com pontas estreitas, secundários menores e fissuras controladas.
- **O17 — Núcleo Infernal:** Anel de obsidiana e gema quadrada preservados, contraste e relevo no leito.
- **O18 — Escória Demoníaca:** Escória irregular com camadas rochosas e brilho restrito a veios/cristais.
- **O19 — Fragmento Vazio:** Fragmentos escalonados preservados; quinas e separação material de rocha/void.
- **O20 — Cristal Anômalo:** Prisma central enriquecido por brotos menores, contraste ciano/violeta e encaixes.
- **O21 — Nullstone:** Monólito preto preservado, fendas estreitas e facetas de rugosidade contrastante.
- **O22 — Prisma Galáctico:** Prisma herói preservado; pequenos periféricos e graduação de facetas saturadas.
- **O23 — Singularidade Lapidada:** Eixos cruzados e aro mantidos; pedra mais estruturada e energia contida.
- **O24 — Coração do Horizonte:** Prisma assimétrico enriquecido com pequenos cristais e cinco ressaltos de estrela integrados à base.

## Evidência técnica e limites

- 29/29 modelos V02 reabertos e GLBs reimportados com a mesma contagem de triângulos e malhas. Transformações identidade, coordenadas finitas, sem arestas abertas/não manifold ou faces de área zero nas malhas GAME verificadas.
- 15 renders de picaretas e 72 renders de minérios em 1024 × 1024; 24 comparações em 1536 × 1024; pranchas de pilotos em 2560 × 1024. A aprovação artística continua pendente.
- Os modelos preservam pivô comum. Picaretas usam referência de pega na origem; minérios usam referência de base. A escala em studs, colisores, normalização de importação, soldas dos fragmentos da Void e desempenho mobile ainda precisam de teste no Roblox Studio.
- Não foi modificado o projeto Roblox. Texturas/atlas, VFX runtime, colisão no Studio e testes de gameplay não foram produzidos nesta etapa. O uso de Principled PBR evita nós procedurais exclusivos, mas a aparência da emissão no importador precisa ser conferida.
- A aura e os fragmentos orbitais de prévia não devem virar colisores físicos independentes. A implementação deve usar efeitos visuais de evento, com variante de movimento reduzido.
- O Blender Debian não oferece OpenImageDenoise; as imagens usam Cycles sem denoiser. Ainda pode haver ruído fino em áreas de sombra, sobretudo nas comparações.
- Detalhes de sulcos e filigranas são geometrias pequenas. Precisam ser avaliados na distância real de câmera; podem ser omitidos de LODs distantes.

[Dados completos de validação](Art_V02_Validation.json) · [Dados de silhueta](Pickaxe_V02_Silhouette_Review.json)

## Reconstrução

```sh
mkdir -p /tmp/blender-xdg/config /tmp/blender-xdg/cache
XDG_CONFIG_HOME=/tmp/blender-xdg/config XDG_CACHE_HOME=/tmp/blender-xdg/cache blender -b -t 5 --python-exit-code 1 --python scripts/build_pickaxe_pilots_v02.py -- --all
XDG_CONFIG_HOME=/tmp/blender-xdg/config XDG_CACHE_HOME=/tmp/blender-xdg/cache blender -b -t 5 --python-exit-code 1 --python scripts/review_pickaxe_silhouettes_v02.py
XDG_CONFIG_HOME=/tmp/blender-xdg/config XDG_CACHE_HOME=/tmp/blender-xdg/cache blender -b -t 5 --python-exit-code 1 --python scripts/refine_ores_v02.py -- --all
XDG_CONFIG_HOME=/tmp/blender-xdg/config XDG_CACHE_HOME=/tmp/blender-xdg/cache blender -b -t 5 --python-exit-code 1 --python scripts/review_ores_v02.py
XDG_CONFIG_HOME=/tmp/blender-xdg/config XDG_CACHE_HOME=/tmp/blender-xdg/cache blender -b -t 2 --python-exit-code 1 --python scripts/finalize_art_v02.py
XDG_CONFIG_HOME=/tmp/blender-xdg/config XDG_CACHE_HOME=/tmp/blender-xdg/cache blender -b -t 2 --python-exit-code 1 --python scripts/validate_art_v02.py
python3 scripts/write_art_v02_review.py
```
