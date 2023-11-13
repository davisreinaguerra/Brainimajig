import bpy

def open_structure(structure_code, color):
    # find and create structure
    structure_code_string = str(structure_code)
    
    file_path_structure = "C:\\Users\\davis\\.brainglobe\\allen_mouse_100um_v1.2\\meshes\\" + structure_code_string + ".obj"
    bpy.ops.wm.obj_import(filepath=file_path_structure, clamp_size=0.01, forward_axis='Z', up_axis='NEGATIVE_Y')
    
    # Get active object
    activeObject = bpy.context.active_object
    
    # Rename object
    activeObject.name = structure_code_string
    
    # Add material
    mat = bpy.data.materials.new(name=structure_code_string) #set new material to variable
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