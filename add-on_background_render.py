bl_info = {
    'name' : 'Background Render',
    'author' : 'Hans Willem Gijzel',
    'version' : (1, 0),
    'blender' : (2, 80, 0  ),
    'location' : 'View 3D > Tools > My Addon',
    'description' : 'Creates Bat File',
    'warning' : '',
    'wiki_url' : '',
    'category' : 'Render'
    }

#imports
import bpy
import subprocess
import os

def main_openFolder():
    subprocess.Popen('explorer ' + bpy.path.abspath('//'))

def main_createBatFile():
    batfile = os.path.join(os.path.dirname(bpy.data.filepath), 'bg_render.bat')
    f = open(batfile, 'w+')
    render_string = '"' + bpy.app.binary_path + '" -b "' + str(bpy.data.filepath) + '" -x 1 -a' + '\n'
    f.write(render_string)
    f.close()
    main_openFolder()
    
#panel class
class BACKGROUNDRENDER_PT_Panel(bpy.types.Panel):
    #panel attributes
    """Tooltip"""
    bl_label = 'Background Render'
    bl_idname = 'BACKGROUNDRENDER_PT_Panel'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Background Render'
    
    #draw loop
    def draw(self, context):
        layout = self.layout
        col = layout.column(align = True)
        col.operator('script.bgrender_create_bat_file', text='Create .bat File')

#operator class
class CREATEBATFILE_OT_Operator(bpy.types.Operator):
    #operator attributes
    """Tooltip"""
    bl_label = 'Create Bat File'
    bl_idname = 'script.bgrender_create_bat_file'
    
    #poll - if the poll function returns False, the button will be greyed out
    @classmethod
    def poll(cls, context):
        return 2 > 1
    
    #execute
    def execute(self, context):
        main_createBatFile()
        return {'FINISHED'}

#registration
classes = (
    BACKGROUNDRENDER_PT_Panel,
    CREATEBATFILE_OT_Operator,
)

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)

#enable to test the addon by running this script
if __name__ == '__main__':
    register()
