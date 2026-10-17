# Catálogo 3D V01 — BrainHot Mining

Este catálogo reúne os 24 conceitos de minérios e as 28 picaretas da bíblia de produção V1. O03 e O04 são pilotos anteriores preservados; este lote acrescenta 22 minérios e 28 picaretas. É uma **primeira passada visual para revisão**, não aprovação de arte final ou integração no Roblox Studio. Os IDs dos manifests são propostas conceituais e não foram associados a IDs funcionais do jogo.

## Verificação técnica

- Blender 4.3.2 executou o gerador para os 50 novos assets. Cada `.blend` foi reaberto e cada GLB reimportado. As 50 comparações de triângulos e contagens de malhas passaram.
- As 150 novas renderizações são PNGs de 1024 × 1024 pixels. Somadas às seis imagens dos pilotos, o repositório contém 156 PNGs, 52 modelos `.blend` e 52 GLBs.
- Todas as malhas novas têm transformações aplicadas e pivô na origem. Minérios novos: 320–984 triângulos na versão GAME; picaretas: 708–976. A bíblia sugere 500–3.000 para minérios e 1.500–5.000 para picaretas como referência de prototipagem, não limite oficial. Onze minérios novos e todas as picaretas estão abaixo dessas faixas por desenho simples, e devem ser avaliados visualmente, especialmente em tela mobile.
- O validador e os dados por peça estão em [`Catalog_Validation.json`](Catalog_Validation.json). O script de reconstrução está em [`build_catalog.py`](../scripts/build_catalog.py), e o teste automatizado em [`validate_catalog.py`](../scripts/validate_catalog.py).

## Leitura artística e prioridades de revisão

1. **Diferenciar picaretas por família e tier.** O cabo e a barra transversal compartilham uma estrutura base. P05/P13/P18/P24 têm esporas de foice, P17/P26/P28 têm aro e P27/P28 têm chifres, mas a silhueta total ainda é semelhante. P28, em especial, não comunica sozinho o teto de qualidade final descrito na bíblia.
2. **Refinar formas únicas dos minérios.** O12 lê como duas gemas arredondadas sobre uma ponta, em vez de um coração angular integrado; O11 usa aro contínuo em vez de duas conchas; O24 usa base rochosa comum em vez de estrela. O01/O02/O05/O19–O21 também podem ganhar escultura e detalhe focado.
3. **Melhorar apresentação.** Os PNGs têm ruído visível porque o Blender Debian não inclui OpenImageDenoise. Um render de aprovação deve usar mais amostras ou um denoiser disponível no ambiente.
4. **Validar materiais no Roblox Studio.** O GLB transporta cores e materiais básicos, mas não há atlas UV/bake nem teste de aparência, escala em studs, colisão, desempenho com muitas instâncias ou LOD no Studio. Não há VFX de golpe/quebra, economia, drops ou alteração do projeto Roblox.

## Minérios

| ID | Conceito | Triângulos GAME | Revisão | Arquivos |
| --- | --- | ---: | --- | --- |
| O01 | Pedra Brumosa | 852 | [V01](../renders/BH_ORE_O01_Pedra_Brumosa_V01_Iso.png) | [.blend](../models/BH_ORE_O01_Pedra_Brumosa_V01.blend) · [GLB](../exports/BH_ORE_O01_Pedra_Brumosa_V01.glb) |
| O02 | Quartzo de Abóbora | 352 | [V01](../renders/BH_ORE_O02_Quartzo_de_Abobora_V01_Iso.png) | [.blend](../models/BH_ORE_O02_Quartzo_de_Abobora_V01.blend) · [GLB](../exports/BH_ORE_O02_Quartzo_de_Abobora_V01.glb) |
| O03 | Cristal Crepuscular | 836 | [piloto](../renders/Twilight_Crystal_Iso.png) | [.blend](../models/Twilight_Crystal_Ore.blend) · [GLB](../exports/Twilight_Crystal_Ore.glb) |
| O04 | Âmbar Espiritual | 692 | [piloto](../renders/Spirit_Amber_Iso.png) | [.blend](../models/Spirit_Amber_Ore.blend) · [GLB](../exports/Spirit_Amber_Ore.glb) |
| O05 | Rocha das Runas | 468 | [V01](../renders/BH_ORE_O05_Rocha_das_Runas_V01_Iso.png) | [.blend](../models/BH_ORE_O05_Rocha_das_Runas_V01.blend) · [GLB](../exports/BH_ORE_O05_Rocha_das_Runas_V01.glb) |
| O06 | Ametista de Colheita | 416 | [V01](../renders/BH_ORE_O06_Ametista_de_Colheita_V01_Iso.png) | [.blend](../models/BH_ORE_O06_Ametista_de_Colheita_V01.blend) · [GLB](../exports/BH_ORE_O06_Ametista_de_Colheita_V01.glb) |
| O07 | Pedra Lunar | 732 | [V01](../renders/BH_ORE_O07_Pedra_Lunar_V01_Iso.png) | [.blend](../models/BH_ORE_O07_Pedra_Lunar_V01.blend) · [GLB](../exports/BH_ORE_O07_Pedra_Lunar_V01.glb) |
| O08 | Quartzo Espectral | 460 | [V01](../renders/BH_ORE_O08_Quartzo_Espectral_V01_Iso.png) | [.blend](../models/BH_ORE_O08_Quartzo_Espectral_V01.blend) · [GLB](../exports/BH_ORE_O08_Quartzo_Espectral_V01.glb) |
| O09 | Safira Sepulcral | 740 | [V01](../renders/BH_ORE_O09_Safira_Sepulcral_V01_Iso.png) | [.blend](../models/BH_ORE_O09_Safira_Sepulcral_V01.blend) · [GLB](../exports/BH_ORE_O09_Safira_Sepulcral_V01.glb) |
| O10 | Gelo Fantasma | 540 | [V01](../renders/BH_ORE_O10_Gelo_Fantasma_V01_Iso.png) | [.blend](../models/BH_ORE_O10_Gelo_Fantasma_V01.blend) · [GLB](../exports/BH_ORE_O10_Gelo_Fantasma_V01.glb) |
| O11 | Eclipse Enjaulado | 596 | [V01](../renders/BH_ORE_O11_Eclipse_Enjaulado_V01_Iso.png) | [.blend](../models/BH_ORE_O11_Eclipse_Enjaulado_V01.blend) · [GLB](../exports/BH_ORE_O11_Eclipse_Enjaulado_V01.glb) |
| O12 | Coração Lanternado | 484 | [V01](../renders/BH_ORE_O12_Coracao_Lanternado_V01_Iso.png) | [.blend](../models/BH_ORE_O12_Coracao_Lanternado_V01.blend) · [GLB](../exports/BH_ORE_O12_Coracao_Lanternado_V01.glb) |
| O13 | Ferro das Cinzas | 852 | [V01](../renders/BH_ORE_O13_Ferro_das_Cinzas_V01_Iso.png) | [.blend](../models/BH_ORE_O13_Ferro_das_Cinzas_V01.blend) · [GLB](../exports/BH_ORE_O13_Ferro_das_Cinzas_V01.glb) |
| O14 | Cristal de Brasa | 756 | [V01](../renders/BH_ORE_O14_Cristal_de_Brasa_V01_Iso.png) | [.blend](../models/BH_ORE_O14_Cristal_de_Brasa_V01.blend) · [GLB](../exports/BH_ORE_O14_Cristal_de_Brasa_V01.glb) |
| O15 | Obsidiana Ritual | 456 | [V01](../renders/BH_ORE_O15_Obsidiana_Ritual_V01_Iso.png) | [.blend](../models/BH_ORE_O15_Obsidiana_Ritual_V01.blend) · [GLB](../exports/BH_ORE_O15_Obsidiana_Ritual_V01.glb) |
| O16 | Rubi de Magma | 624 | [V01](../renders/BH_ORE_O16_Rubi_de_Magma_V01_Iso.png) | [.blend](../models/BH_ORE_O16_Rubi_de_Magma_V01.blend) · [GLB](../exports/BH_ORE_O16_Rubi_de_Magma_V01.glb) |
| O17 | Núcleo Infernal | 468 | [V01](../renders/BH_ORE_O17_Nucleo_Infernal_V01_Iso.png) | [.blend](../models/BH_ORE_O17_Nucleo_Infernal_V01.blend) · [GLB](../exports/BH_ORE_O17_Nucleo_Infernal_V01.glb) |
| O18 | Escória Demoníaca | 984 | [V01](../renders/BH_ORE_O18_Escoria_Demoniaca_V01_Iso.png) | [.blend](../models/BH_ORE_O18_Escoria_Demoniaca_V01.blend) · [GLB](../exports/BH_ORE_O18_Escoria_Demoniaca_V01.glb) |
| O19 | Fragmento Vazio | 320 | [V01](../renders/BH_ORE_O19_Fragmento_Vazio_V01_Iso.png) | [.blend](../models/BH_ORE_O19_Fragmento_Vazio_V01.blend) · [GLB](../exports/BH_ORE_O19_Fragmento_Vazio_V01.glb) |
| O20 | Cristal Anômalo | 364 | [V01](../renders/BH_ORE_O20_Cristal_Anomalo_V01_Iso.png) | [.blend](../models/BH_ORE_O20_Cristal_Anomalo_V01.blend) · [GLB](../exports/BH_ORE_O20_Cristal_Anomalo_V01.glb) |
| O21 | Nullstone | 320 | [V01](../renders/BH_ORE_O21_Nullstone_V01_Iso.png) | [.blend](../models/BH_ORE_O21_Nullstone_V01.blend) · [GLB](../exports/BH_ORE_O21_Nullstone_V01.glb) |
| O22 | Prisma Galáctico | 548 | [V01](../renders/BH_ORE_O22_Prisma_Galactico_V01_Iso.png) | [.blend](../models/BH_ORE_O22_Prisma_Galactico_V01.blend) · [GLB](../exports/BH_ORE_O22_Prisma_Galactico_V01.glb) |
| O23 | Singularidade Lapidada | 480 | [V01](../renders/BH_ORE_O23_Singularidade_Lapidada_V01_Iso.png) | [.blend](../models/BH_ORE_O23_Singularidade_Lapidada_V01.blend) · [GLB](../exports/BH_ORE_O23_Singularidade_Lapidada_V01.glb) |
| O24 | Coração do Horizonte | 592 | [V01](../renders/BH_ORE_O24_Coracao_do_Horizonte_V01_Iso.png) | [.blend](../models/BH_ORE_O24_Coracao_do_Horizonte_V01.blend) · [GLB](../exports/BH_ORE_O24_Coracao_do_Horizonte_V01.glb) |

## Picaretas

| ID | Conceito | Triângulos GAME | Revisão | Arquivos |
| --- | --- | ---: | --- | --- |
| P01 | Picareta Rúnica de Pedra | 772 | [V01](../renders/BH_PICK_P01_Picareta_Runica_de_Pedra_V01_Iso.png) | [.blend](../models/BH_PICK_P01_Picareta_Runica_de_Pedra_V01.blend) · [GLB](../exports/BH_PICK_P01_Picareta_Runica_de_Pedra_V01.glb) |
| P02 | Picareta de Cobre Encantado | 772 | [V01](../renders/BH_PICK_P02_Picareta_de_Cobre_Encantado_V01_Iso.png) | [.blend](../models/BH_PICK_P02_Picareta_de_Cobre_Encantado_V01.blend) · [GLB](../exports/BH_PICK_P02_Picareta_de_Cobre_Encantado_V01.glb) |
| P03 | Picareta Abóbora Bruta | 772 | [V01](../renders/BH_PICK_P03_Picareta_Abobora_Bruta_V01_Iso.png) | [.blend](../models/BH_PICK_P03_Picareta_Abobora_Bruta_V01.blend) · [GLB](../exports/BH_PICK_P03_Picareta_Abobora_Bruta_V01.glb) |
| P04 | Picareta de Cristal Brumoso | 716 | [V01](../renders/BH_PICK_P04_Picareta_de_Cristal_Brumoso_V01_Iso.png) | [.blend](../models/BH_PICK_P04_Picareta_de_Cristal_Brumoso_V01.blend) · [GLB](../exports/BH_PICK_P04_Picareta_de_Cristal_Brumoso_V01.glb) |
| P05 | Colheita Sombria | 808 | [V01](../renders/BH_PICK_P05_Colheita_Sombria_V01_Iso.png) | [.blend](../models/BH_PICK_P05_Colheita_Sombria_V01.blend) · [GLB](../exports/BH_PICK_P05_Colheita_Sombria_V01.glb) |
| P06 | Presa Espectral | 772 | [V01](../renders/BH_PICK_P06_Presa_Espectral_V01_Iso.png) | [.blend](../models/BH_PICK_P06_Presa_Espectral_V01.blend) · [GLB](../exports/BH_PICK_P06_Presa_Espectral_V01.glb) |
| P07 | Marreta Lunar Fragmentada | 792 | [V01](../renders/BH_PICK_P07_Marreta_Lunar_Fragmentada_V01_Iso.png) | [.blend](../models/BH_PICK_P07_Marreta_Lunar_Fragmentada_V01.blend) · [GLB](../exports/BH_PICK_P07_Marreta_Lunar_Fragmentada_V01.glb) |
| P08 | Picareta Fúria de Safira | 716 | [V01](../renders/BH_PICK_P08_Picareta_Furia_de_Safira_V01_Iso.png) | [.blend](../models/BH_PICK_P08_Picareta_Furia_de_Safira_V01.blend) · [GLB](../exports/BH_PICK_P08_Picareta_Furia_de_Safira_V01.glb) |
| P09 | Picareta do Espinhal Assombrado | 796 | [V01](../renders/BH_PICK_P09_Picareta_do_Espinhal_Assombrado_V01_Iso.png) | [.blend](../models/BH_PICK_P09_Picareta_do_Espinhal_Assombrado_V01.blend) · [GLB](../exports/BH_PICK_P09_Picareta_do_Espinhal_Assombrado_V01.glb) |
| P10 | Picareta Gelo Fantasma | 716 | [V01](../renders/BH_PICK_P10_Picareta_Gelo_Fantasma_V01_Iso.png) | [.blend](../models/BH_PICK_P10_Picareta_Gelo_Fantasma_V01.blend) · [GLB](../exports/BH_PICK_P10_Picareta_Gelo_Fantasma_V01.glb) |
| P11 | Rachadora das Ruínas | 792 | [V01](../renders/BH_PICK_P11_Rachadora_das_Ruinas_V01_Iso.png) | [.blend](../models/BH_PICK_P11_Rachadora_das_Ruinas_V01.blend) · [GLB](../exports/BH_PICK_P11_Rachadora_das_Ruinas_V01.glb) |
| P12 | Picareta de Magma Profano | 772 | [V01](../renders/BH_PICK_P12_Picareta_de_Magma_Profano_V01_Iso.png) | [.blend](../models/BH_PICK_P12_Picareta_de_Magma_Profano_V01.blend) · [GLB](../exports/BH_PICK_P12_Picareta_de_Magma_Profano_V01.glb) |
| P13 | Foice de Ecos Noturnos | 808 | [V01](../renders/BH_PICK_P13_Foice_de_Ecos_Noturnos_V01_Iso.png) | [.blend](../models/BH_PICK_P13_Foice_de_Ecos_Noturnos_V01.blend) · [GLB](../exports/BH_PICK_P13_Foice_de_Ecos_Noturnos_V01.glb) |
| P14 | Picareta de Quartzo Celestial | 716 | [V01](../renders/BH_PICK_P14_Picareta_de_Quartzo_Celestial_V01_Iso.png) | [.blend](../models/BH_PICK_P14_Picareta_de_Quartzo_Celestial_V01.blend) · [GLB](../exports/BH_PICK_P14_Picareta_de_Quartzo_Celestial_V01.glb) |
| P15 | Picareta Véu das Almas | 772 | [V01](../renders/BH_PICK_P15_Picareta_Veu_das_Almas_V01_Iso.png) | [.blend](../models/BH_PICK_P15_Picareta_Veu_das_Almas_V01.blend) · [GLB](../exports/BH_PICK_P15_Picareta_Veu_das_Almas_V01.glb) |
| P16 | Fragmento Void | 716 | [V01](../renders/BH_PICK_P16_Fragmento_Void_V01_Iso.png) | [.blend](../models/BH_PICK_P16_Fragmento_Void_V01.blend) · [GLB](../exports/BH_PICK_P16_Fragmento_Void_V01.glb) |
| P17 | Orbital do Vazio | 864 | [V01](../renders/BH_PICK_P17_Orbital_do_Vazio_V01_Iso.png) | [.blend](../models/BH_PICK_P17_Orbital_do_Vazio_V01.blend) · [GLB](../exports/BH_PICK_P17_Orbital_do_Vazio_V01.glb) |
| P18 | Ceifadora Demoníaca | 808 | [V01](../renders/BH_PICK_P18_Ceifadora_Demoniaca_V01_Iso.png) | [.blend](../models/BH_PICK_P18_Ceifadora_Demoniaca_V01.blend) · [GLB](../exports/BH_PICK_P18_Ceifadora_Demoniaca_V01.glb) |
| P19 | Picareta Divindade Aurora | 716 | [V01](../renders/BH_PICK_P19_Picareta_Divindade_Aurora_V01_Iso.png) | [.blend](../models/BH_PICK_P19_Picareta_Divindade_Aurora_V01.blend) · [GLB](../exports/BH_PICK_P19_Picareta_Divindade_Aurora_V01.glb) |
| P20 | Picareta Glacial Abissal | 716 | [V01](../renders/BH_PICK_P20_Picareta_Glacial_Abissal_V01_Iso.png) | [.blend](../models/BH_PICK_P20_Picareta_Glacial_Abissal_V01.blend) · [GLB](../exports/BH_PICK_P20_Picareta_Glacial_Abissal_V01.glb) |
| P21 | Picareta Glitch Hacker | 708 | [V01](../renders/BH_PICK_P21_Picareta_Glitch_Hacker_V01_Iso.png) | [.blend](../models/BH_PICK_P21_Picareta_Glitch_Hacker_V01.blend) · [GLB](../exports/BH_PICK_P21_Picareta_Glitch_Hacker_V01.glb) |
| P22 | Código Fantasma | 708 | [V01](../renders/BH_PICK_P22_Codigo_Fantasma_V01_Iso.png) | [.blend](../models/BH_PICK_P22_Codigo_Fantasma_V01.blend) · [GLB](../exports/BH_PICK_P22_Codigo_Fantasma_V01.glb) |
| P23 | Picareta Rei Abóbora | 772 | [V01](../renders/BH_PICK_P23_Picareta_Rei_Abobora_V01_Iso.png) | [.blend](../models/BH_PICK_P23_Picareta_Rei_Abobora_V01.blend) · [GLB](../exports/BH_PICK_P23_Picareta_Rei_Abobora_V01.glb) |
| P24 | Ceifadora do Crepúsculo | 808 | [V01](../renders/BH_PICK_P24_Ceifadora_do_Crepusculo_V01_Iso.png) | [.blend](../models/BH_PICK_P24_Ceifadora_do_Crepusculo_V01.blend) · [GLB](../exports/BH_PICK_P24_Ceifadora_do_Crepusculo_V01.glb) |
| P25 | Picareta Natal Sombrio | 716 | [V01](../renders/BH_PICK_P25_Picareta_Natal_Sombrio_V01_Iso.png) | [.blend](../models/BH_PICK_P25_Picareta_Natal_Sombrio_V01.blend) · [GLB](../exports/BH_PICK_P25_Picareta_Natal_Sombrio_V01.glb) |
| P26 | Picareta Eclipse Enjaulado | 864 | [V01](../renders/BH_PICK_P26_Picareta_Eclipse_Enjaulado_V01_Iso.png) | [.blend](../models/BH_PICK_P26_Picareta_Eclipse_Enjaulado_V01.blend) · [GLB](../exports/BH_PICK_P26_Picareta_Eclipse_Enjaulado_V01.glb) |
| P27 | Picareta Dragão Mineral | 884 | [V01](../renders/BH_PICK_P27_Picareta_Dragao_Mineral_V01_Iso.png) | [.blend](../models/BH_PICK_P27_Picareta_Dragao_Mineral_V01.blend) · [GLB](../exports/BH_PICK_P27_Picareta_Dragao_Mineral_V01.glb) |
| P28 | Picareta Núcleo Prime | 976 | [V01](../renders/BH_PICK_P28_Picareta_Nucleo_Prime_V01_Iso.png) | [.blend](../models/BH_PICK_P28_Picareta_Nucleo_Prime_V01.blend) · [GLB](../exports/BH_PICK_P28_Picareta_Nucleo_Prime_V01.glb) |

## Reprodução

Na raiz do checkout:

```sh
mkdir -p /tmp/blender-xdg/config /tmp/blender-xdg/cache
XDG_CONFIG_HOME=/tmp/blender-xdg/config XDG_CACHE_HOME=/tmp/blender-xdg/cache blender -b -t 4 --python scripts/build_catalog.py -- --id O01
XDG_CONFIG_HOME=/tmp/blender-xdg/config XDG_CACHE_HOME=/tmp/blender-xdg/cache blender -b -t 2 --python scripts/validate_catalog.py
```

Para reconstruir todo o lote, use `--all` no lugar de `--id O01`. O gerador preserva O03 e O04. A reconstrução sobrescreve apenas os arquivos gerados dos 50 assets deste lote.
