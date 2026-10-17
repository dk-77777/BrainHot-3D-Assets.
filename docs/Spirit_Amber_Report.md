# Âmbar Espiritual — piloto 3D O04

Segundo minério piloto da bíblia de produção V1. A direção O04 pede resina fossilizada irregular, luz de vaga-lume aprisionada, rocha plana, paleta mel/dourado/madeira escura e sem simulação de inseto realista. O modelo usa inclusões luminosas abstratas e raízes fossilizadas para comunicar a ideia sem introduzir insetos ou partículas permanentes.

## Entrega

- `models/Spirit_Amber_Ore.blend`: mestre editável com coleções `01 MASTER`, `02 GAME` e `90 STUDIO`.
- `exports/Spirit_Amber_Ore.glb`: malhas otimizadas da coleção `02 GAME`, sem iluminação, câmera ou piso.
- `renders/Spirit_Amber_{Front,Iso,Back}.png`: vistas de 1024 × 1024 pixels.
- `scripts/build_spirit_amber_ore.py`: script bpy determinístico para Blender 4.3.2.

A geometria é formada por base rochosa facetada e baixa, quatro massas irregulares de resina, inclusões emissivas e tiras de raiz fossilizada. Materiais Principled BSDF usam cor base, rugosidade, metalicidade e emissão. A versão de jogo evita transparência e nós exclusivos do Blender. Os objetos têm pivô comum na origem e transformações aplicadas.

## Verificação

O script foi executado no Blender 4.3.2. O `.blend` foi salvo e reaberto em processo separado. O GLB foi reimportado, com contagem idêntica à versão de jogo. As três imagens foram verificadas como PNG de 1024 × 1024 pixels e inspecionadas visualmente.

| Versão | Malhas | Triângulos | Dimensões X × Y × Z |
| --- | ---: | ---: | --- |
| MASTER | 24 | 1.668 | 2,830 × 2,935 × 1,817 |
| GAME / GLB | 14 | 692 | 2,617 × 2,946 × 1,814 |

O GLB reimportado contém 14 malhas, 692 triângulos e nove materiais. As transformações das duas coleções são identidade. A versão GAME fica dentro do intervalo sugerido para prototipagem de minérios (500–3.000 triângulos), que não é limite oficial do Roblox.

## Limitações para avaliação

- As inclusões luminosas são formas opacas emissivas, não luzes suspensas dentro de resina transparente. Isso preserva um material simples para exportação, mas reduz a sensação de profundidade do âmbar. Uma futura revisão pode usar atlas com pintura de inclusões ou validar transparência específica no Studio.
- Emissão, brilho, colisão, escala em studs, LOD e desempenho com muitas instâncias ainda exigem teste no Roblox Studio. A iluminação do estúdio de renderização não é exportada.
- O arquivo não inclui VFX de quebra nem altera IDs, economia, drops ou o projeto Roblox. A associação do conceito O04 a um item funcional ainda requer o mapeamento indicado pela bíblia.
- O Blender Debian deste ambiente não contém OpenImageDenoise; o render usa Cycles sem denoiser. Avisos EGL em modo headless podem aparecer sem impedir a geração.

Para reconstruir na raiz do checkout:

```sh
mkdir -p /tmp/blender-xdg/config /tmp/blender-xdg/cache
XDG_CONFIG_HOME=/tmp/blender-xdg/config XDG_CACHE_HOME=/tmp/blender-xdg/cache blender -b -t 4 --python scripts/build_spirit_amber_ore.py
```
