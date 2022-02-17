import bpy
from random import randint

shapeNumber = 9
for s in range(0, shapeNumber):
    x_base =
    x_sphere = 0
    y_sphere = 0
    z_sphere = s

    x_torus = x_sphere + 1
    y_torus = 0
    z_torus = s

    x_torus2 = x_sphere - 1
    y_torus2 = 0
    z_torus2 = s

    bpy.ops.mesh.primitive_ico_sphere_add(location = [x_sphere, y_sphere, z_sphere])

    if s % 2 is 0:
        bpy.ops.mesh.primitive_torus_add(location = [x_torus, y_torus, z_torus])
    else:
        bpy.ops.mesh.primitive_torus_add(location = [x_torus2, y_torus2, z_torus2])
