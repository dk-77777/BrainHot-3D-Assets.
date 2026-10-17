# Cristal do Crepúsculo — piloto 3D

Piloto visual do minério O03, “Cristal Crepuscular”, da bíblia de produção V1. A referência orientou a base de rocha escura, o aglomerado radial de ametista, a paleta violeta/lavanda/carvão e as linhas claras. Este pacote não altera o projeto Roblox Studio nem implementa economia ou VFX de jogo.

## Arquivos

- `models/Twilight_Crystal_Ore.blend`: cena editável com coleções `01 MASTER`, `02 GAME` e `90 STUDIO`.
- `exports/Twilight_Crystal_Ore.glb`: apenas as malhas da coleção `02 GAME`; sem câmera, luz ou piso.
- `renders/Twilight_Crystal_{Front,Iso,Back}.png`: três vistas de 1024 × 1024 pixels.
- `scripts/build_twilight_ore.py`: geração determinística em Blender 4.3.2.

## Construção

A base é formada por malhas de anéis irregulares facetados; sete prismas de ametista têm seção e comprimentos variados. Há núcleo violeta, fissuras modeladas como malha e pequenos selos metálicos. Os materiais usam Principled BSDF com cor base, metalicidade, rugosidade e emissão moderada; a exportação GLB não depende de nós procedurais. O pivô de cada objeto está na origem comum da peça e as transformações foram aplicadas. A escala é de referência e requer calibração no Studio.

## Validação executada

Blender 4.3.2 executou o script, salvou o `.blend`, exportou o GLB e renderizou as três vistas. O `.blend` foi reaberto em um novo processo. O GLB foi importado de volta no Blender.

| Versão | Objetos de malha | Triângulos | Dimensões aproximadas (X × Y × Z) |
| --- | ---: | ---: | --- |
| MASTER | 29 | 1.808 | 3,017 × 2,895 × 2,378 |
| GAME / GLB | 18 | 836 | 2,947 × 3,011 × 2,350 |

O GLB reimportado manteve 18 objetos de malha, 836 triângulos e 10 materiais. As transformações dos objetos das duas coleções são identidade. Os três arquivos PNG foram verificados como 1024 × 1024 pixels e inspecionados visualmente.

## Limitações e próxima revisão

- A iluminação de estúdio realça a ametista; a leitura das fissuras é sutil e alguns trechos parecem linhas elevadas. Refinar seu encaixe na rocha pode melhorar a peça.
- O núcleo é uma malha sólida com emissão. A aparência do brilho e dos materiais em Roblox Studio ainda não foi testada; a luz de estúdio não acompanha o GLB.
- Não há texturas UV/bake. Se o importador do Studio não preservar cores e emissão do GLB como esperado, criar um atlas de cor e configurar `SurfaceAppearance` ou materiais nativos em etapa posterior.
- Escala, colisão, LOD e desempenho com muitas instâncias exigem teste no jogo antes de aprovação final. O orçamento de 836 triângulos fica na faixa sugerida para prototipagem de minério na bíblia (500–3.000), que não é limite oficial.

Para reconstruir no checkout:

```sh
mkdir -p /tmp/blender-xdg/config /tmp/blender-xdg/cache
XDG_CONFIG_HOME=/tmp/blender-xdg/config XDG_CACHE_HOME=/tmp/blender-xdg/cache blender -b -t 4 --python scripts/build_twilight_ore.py
```

O pacote Debian do Blender deste ambiente não inclui OpenImageDenoise, então o script desativa denoising para renderizar no Cycles. Podem aparecer avisos EGL em modo headless, mesmo com exportação e renderização concluídas.
