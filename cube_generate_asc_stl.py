# -*- encoding: utf-8 -*-
import struct

# infile = open('cube.stl', 'rb') #import file
out = open('generated_cube_ascii.stl', 'w') #export file

# data = infile.read()
# data = data.decode('cp1252')


out.write("solid ")

faces = [[[-1, 0, 0],    [0, 0 ,0], [0, 0, 1], [0, 1, 0]],
         [[-1, 0, 0],    [0, 1 ,0], [0, 0, 1], [0, 1, 1]],
         [[1, 0, 0],     [1, 0 ,1], [1, 0, 0], [1, 1, 0]],
         [[1, 0, 0],     [1, 0 ,1], [1, 1, 0], [1, 1, 2]],
         [[0, -1, 0],    [1, 0 ,0], [1, 0, 1], [0, 0, 0]],
         [[0, -1, 0],    [0, 0 ,0], [1, 0, 1], [0, 0, 1]],
         [[0, 1, 0],     [1, 1, 2], [1, 1, 0], [0, 1, 0]],
         [[0, 1, 0],     [1, 1, 2], [0, 1, 0], [0, 1, 1]],
         [[0, 0, -1],    [0, 1, 0], [1, 1, 0], [0, 0, 0]],
         [[0, 0, -1],    [0, 0, 0], [1, 1, 0], [1, 0, 0]],
         [[0, 0, 1],     [1, 1, 2], [0, 1, 1], [0, 0, 1]],
         [[0, 0, 1],     [1, 1, 2], [0, 0, 1], [1, 0, 1]]]


out.write("Cube Generated ASCII")
out.write("\n")

number = len(faces)
print(f"number: {number}")

for x in range(0, number):
    out.write("facet normal ")

    xc = faces[x][0][0]
    yc = faces[x][0][1]
    zc = faces[x][0][2]

    out.write(f"{xc} {yc} {zc}")
    out.write("\n")
    out.write("\t")

    out.write("outer loop\n")

    for y in range(1, 4):
        out.write("\t\t")
        out.write("vertex ")

        xc = faces[x][y][0]
        yc = faces[x][y][1]
        zc = faces[x][y][2]

        out.write(f"{xc} {yc} {zc}")
        out.write("\n")

    out.write("\t")
    out.write("endloop\n")
    out.write("endfacet\n")

out.write("endsolid ")
out.write("Cube Generated ASCII")
out.write("\n")
out.close()

print("end")
