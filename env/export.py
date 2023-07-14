# exports single object to single glTF file.
# Copyright https://blog.csdn.net/wangmy1988
# Compatible with Blender 3.3.1
 
import bpy
import os
 
# export to blend file location
basedir = os.path.dirname(bpy.data.filepath)
 
print("START Output path = "+basedir)
outFolder = "output"
 
if not basedir:
    raise Exception("Blend file is not saved")
 
objects = bpy.context.collection.objects
 
def exportfunc(objName):
    name = bpy.path.clean_name(objName)
    fn = os.path.join(basedir, outFolder, name)
 
    # Export gltf
    bpy.ops.export_scene.gltf(filepath=fn + ".glb", export_format="GLB", export_lights=False, use_selection=True)
 
    print("written:", fn)
    return
 
#Deselect all objects
for obj in objects:
    obj.select_set(False)
 
print("===Start save files===")
 
for obj in objects:
    if obj.parent == None:
        if len(obj.children) > 0:
            obj.select_set(True)
            for subObj in obj.children:
                subObj.select_set(True)
 
            # some exporters only use the active object
            #view_layer.objects.active = obj
            exportfunc(obj.name)
            
            #Deselect all objects
            for obj in objects:
                obj.select_set(False)
        else:
            obj.select_set(True)
            exportfunc(obj.name)
            obj.select_set(False)
    
print("All save completed!")