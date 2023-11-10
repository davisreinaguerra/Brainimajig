# Davis' Brain Diagram Maker
import bpy

bpy.ops.object.select_by_type(type="MESH")
bpy.ops.object.delete(use_global=False)

structure_code_pairs = {
    "STRd": 485,
    "GPe": 1022,
    "GPi": 1031,
    "SNr": 381,
    "grey": 8,
    "DR": 872,
    "LC":147,
    "LH": 186
}

color_codes = {
    "purple": (0.65,0.38,1,0.9),
    "teal": (0.4,0.6,1,0.9),
    "wine": (0.1,0.012,0.013,0.9),
    "green": (0.054117, 0.295696, 0.0123723, 0.9),
    "white": (1,1,1,0.01)

}

def open_structure(structure_string, color):
    # find and create structure
    file_path_structure = "/Users/davisreinaguerra/.brainglobe/allen_mouse_10um_v1.2/meshes/" + str(structure_code_pairs[structure_string]) + ".obj"
    bpy.ops.wm.obj_import(filepath=file_path_structure, clamp_size=0.01, forward_axis='Z', up_axis='NEGATIVE_Y')
    
    # Get active object
    activeObject = bpy.context.active_object
    
    # Rename object
    activeObject.name = structure_string
    
    # Add material
    mat = bpy.data.materials.new(name=structure_string) #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = color
    bpy.context.object.active_material.blend_method = 'BLEND'
    
def create_fiber_cannula(length, name):
    # Implanted
    bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(0.125, 0.125, length))
    activeObject = bpy.context.active_object
    activeObject.name = "implant"
    activeObject.dimensions = (0.25, 0.25, length)
    mat = bpy.data.materials.new(name="white_implant") #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (1,1,1,1)
    
    # cannula 
    bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(0.125, 0.125, length))
    activeObject = bpy.context.active_object
    activeObject.name = "cannula"
    activeObject.dimensions = (0.5, 0.5,2)
    activeObject.location = (0,0,length-1)
    mat = bpy.data.materials.new(name="black_base") #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    bpy.context.object.active_material.diffuse_color = (0,0,0,1)
    
    bpy.data.objects["implant"].select_set(True)
    bpy.data.objects["cannula"].select_set(True)
    bpy.ops.object.join()
    activeObject = bpy.context.active_object
    activeObject.name = name
    

open_structure("STRd", color_codes["purple"])
open_structure("GPe", color_codes["teal"])
open_structure("GPi", color_codes["wine"])
open_structure("SNr", color_codes["wine"])
open_structure("DR", color_codes["green"])
open_structure("LC", color_codes["green"])
open_structure("LH", color_codes["green"])
open_structure("grey", color_codes["white"])

# Join, set origin, and snap to cursor
bpy.ops.object.select_by_type(type="MESH")
bpy.ops.object.join()
bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')
bpy.context.object.location = (0,0,0)

# Rename
activeObject = bpy.context.active_object
activeObject.name = "Composition"


create_fiber_cannula(3.5, "cannula3")
