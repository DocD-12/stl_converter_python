# -*- encoding: utf-8 -*-
import struct

infile = open('binary.stl', 'rb') #import file
out = open('ASCII.stl', 'w') #export file

data = infile.read()
# data = data.decode('cp1252')


out.write("solid ")

for x in range(0, 80):
    if not data[x] == 0:
        out.write(chr(data[x]))
    else:
        pass
out.write("\n")

number = data[80] + data[81] + data[82] + data[83]
print(f"number: {number}")

for x in range(0, number):
    out.write("facet normal ")

    xc = bytearray([data[84+x*50], data[85+x*50], data[86+x*50], data[87+x*50]])
    yc = bytearray([data[88+x*50], data[89+x*50], data[90+x*50], data[91+x*50]])
    zc = bytearray([data[92+x*50], data[93+x*50], data[94+x*50], data[95+x*50]])

    out.write(f'{struct.unpack('<f', xc)[0]:.3g}')
    out.write(" ")
    out.write(f'{struct.unpack('<f', yc)[0]:.3f}')
    out.write(" ")
    out.write(f'{struct.unpack('<f', zc)[0]:.3f}')
    out.write("\n")

    out.write("outer loop\n")

    for y in range(1, 4):
        out.write("vertex ")

        xc = data[84+y*12+x*50] + data[85+y*12+x*50] + data[86+y*12+x*50] + data[87+y*12+x*50]
        yc = data[88+y*12+x*50] + data[89+y*12+x*50] + data[90+y*12+x*50] + data[91+y*12+x*50]
        zc = data[92+y*12+x*50] + data[93+y*12+x*50] + data[94+y*12+x*50] + data[95+y*12+x*50]

        out.write(str(xc) + " ")
        out.write(str(yc) + " ")
        out.write(str(zc) + "\n")

    out.write("endloop\n")
    out.write("endfacet\n")

out.close()

print("end")
