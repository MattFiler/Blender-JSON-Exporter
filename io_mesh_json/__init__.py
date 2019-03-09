bl_info = {
    "name":         "JSON Scene Export",
    "author":       "Matt Filer, Nathan Faucett",
    "blender":      (2,6,8),
    "version":      (0,0,1),
    "location":     "File > Export",
    "description":  "Export scene data in a JSON format.",
    "category":     "Export",
    "wiki_url":     "https://github.com/MattFiler/Blender-JSON-Exporter",
    "tracker_url":  "https://github.com/MattFiler/Blender-JSON-Exporter",
}

import bpy
from bpy.props import *
from bpy_extras.io_utils import ExportHelper, ImportHelper


# ################################################################
# Export JSON
# ################################################################

class ExportJSON( bpy.types.Operator, ExportHelper ):
    bl_idname = "export.json"
    bl_label = "Export JSON"

    filename_ext = ".json"
    
    def invoke( self, context, event ):
        return ExportHelper.invoke( self, context, event )
    
    @classmethod
    def poll( cls, context ):
        return context.active_object != None
    
    def execute( self, context ):
        print("Selected: " + context.active_object.name )
        
        if not self.properties.filepath:
            raise Exception("filename not set")
        
        filepath = self.filepath
        
        import io_mesh_json.export_json
        return io_mesh_json.export_json.save( self, context, **self.properties )


# ################################################################
# Common
# ################################################################

def menu_func_export( self, context ):
    default_path = bpy.data.filepath.replace(".blend", ".json")
    self.layout.operator( ExportJSON.bl_idname, text="JSON (.json)").filepath = default_path

def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_export.append(menu_func_export)

def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_file_export.remove(menu_func_export)

if __name__ == "__main__":
    register()