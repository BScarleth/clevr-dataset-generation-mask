import bpy, bpy_extras


def assign_mask_to_object(mask_by_color, width):
    pixel_center = 76800 - ( (96 * width) + 57)
    for color in mask_by_color:
      if pixel_center in mask_by_color[color]:
        print("here", color)

path = '/home/brenda/Escritorio/tmp47s462az.png'
img = bpy.data.images.load(path)
p = list(img.pixels)

"""
D = bpy.data
image_file = 'Image.png' # this refers to an image file loaded into Blender
img = D.images[image_file]
"""

mask_by_color = {}

width = img.size[0] #320
height = img.size[1] #240

print ( "Image size: ", width, " x ", height )

target = [57, 96] # X, Y
print ("Target vector: ", target)
index = (76800*4 ) - ( target[1] * width + target[0] ) * 4

#index = ( 96 * 320 + 57 ) * 4
print ("Field index: ", index)


pixel = [
    img.pixels[index], # RED
    img.pixels[index + 1], # GREEN
    img.pixels[index + 2], # BLUE
    img.pixels[index + 3] # ALPHA
]

#130 213 188
# print the values for debug
print ("R: ", pixel[0])
print ("G: ", pixel[1])
print ("B: ", pixel[2])
print ("A: ", pixel[3])

pixeles_nuevos = []

for i in range(0, len(p), 4):
    temp = (p[i], p[i + 1], p[i + 2], p[i + 3])
    if temp in mask_by_color:
        mask_by_color[temp].append((i/4))
    else:
        pixeles_nuevos.append(i)
        print("pixel y temp", i, " ", temp)
        mask_by_color[temp] = [(i/4)]

assign_mask_to_object(mask_by_color, width= 320)
print(mask_by_color.keys())
print(pixeles_nuevos)
print("funciona")
