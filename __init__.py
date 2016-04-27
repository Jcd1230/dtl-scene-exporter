bl_info = {
	"name": "D2L Scene Exporter",
	"description": "Exports scene in D2L lua format.",
	"author": "Jason Dogariu",
	"version": (1, 0),
	"blender": (2, 72, 0),
	"location": "Export > D2L Scene",
	"warning": "", # used for warning icon and text in addons panel
	"wiki_url": "",
	"tracker_url": "http://developer.blender.org/maniphest/task/create/?project=3&type=Bug",
	"support": "COMMUNITY",
	"category": "Import-Export"
}

import bpy

class D2LSceneExporter(bpy.types.Operator):
	"""Test exporter which just writes hello world"""
	bl_idname = "export.dtl_scene"
	bl_label = "Export DTL scene"

	filepath = bpy.props.StringProperty(subtype="FILE_PATH")

	@classmethod
	def poll(cls, context):
		return context.object is not None

	def execute(self, context):
		file = open(self.filepath, 'w')
		file.write("Hello World " + context.object.name)
		return {'FINISHED'}

	def invoke(self, context, event):
		context.window_manager.fileselect_add(self)
		return {'RUNNING_MODAL'}


def menu_func(self, context):
	self.layout.operator(D2LSceneExporter.bl_idname)

def register():
	bpy.utils.register_class(D2LSceneExporter)
	bpy.types.INFO_MT_file_export.append(menu_func)

def unregister():
	bpy.utils.unregister_class(D2LSceneExporter)
	bpy.types.INFO_MT_file_export.remove(menu_func)

if __name__ == "__main__":
	register()
