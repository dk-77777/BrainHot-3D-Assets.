"""Set clean editable-file visibility after building, preserving model geometry."""
import bpy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
bpy.context.preferences.filepaths.save_version=0
for p in sorted((ROOT/'models').glob('BH_*_V02.blend')):
    bpy.ops.wm.open_mainfile(filepath=str(p))
    bpy.context.scene.unit_settings.system='METRIC';bpy.context.scene.unit_settings.scale_length=1
    for c in bpy.data.collections:
        hidden=c.name.startswith(('00 REFERENCE','02 GAME','03 AURA'))
        if hidden:c.hide_render=True
        for o in c.objects:o.hide_set(hidden)
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.wm.save_as_mainfile(filepath=str(p))
print('VISIBILITY_FINALIZED',len(list((ROOT/'models').glob('BH_*_V02.blend'))),flush=True)
