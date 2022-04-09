import os.path
import subprocess
import bpy


bl_info = {
    'name': 'Background Render',
    'author': 'Hans Willem Gijzel',
    'version': (1, 0),
    'blender': (2, 91, 0),
    'location': 'Properties Panel > Output > Background Render',
    'description': 'Creates a .bat file for background rendering',
    'warning': '',
    'wiki_url': '',
    'category': 'rendering'
}


def main_openFolder():
    subprocess.Popen('explorer ' + bpy.path.abspath('//'))


def main_createBatFile():
    batfile = os.path.join(os.path.dirname(bpy.data.filepath), 'bg_render.bat')
    f = open(batfile, 'w+')
    render_string = '"' + bpy.app.binary_path + '" -b "' + \
        str(bpy.data.filepath) + '" -x 1 -a' + '\n'
    f.write(render_string)
    f.close()
    main_openFolder()


# operator class
class SCRIPT_OT_bg_render(bpy.types.Operator):
    # operator attributes
    """Tooltip"""
    bl_label = 'Create a .bat file'
    bl_idname = 'script.bg_render'

    # poll - if the poll function returns False, the button will be greyed out
    @classmethod
    def poll(cls, context):
        return bpy.data.is_saved

    # execute
    def execute(self, context):
        main_createBatFile()
        return {'FINISHED'}


# panel class
class VIEW_3D_PT_background_render(bpy.types.Panel):
    # panel attributes
    """Tooltip"""
    bl_label = 'Background Render'
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "output"
    bl_category = 'Background Render'

    # draw loop
    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.operator('script.bg_render', text='Create .bat file')


# registration
classes = (
    VIEW_3D_PT_background_render,
    SCRIPT_OT_bg_render
)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)


# enable to test the addon by running this script
if __name__ == '__main__':
    register()
