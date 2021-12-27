import cv2

#image = cv2.imread('/home/brenda/Documentos/independent_study/clevr-dataset-gen/output/images/CLEVR_new_000000.png')

#image = cv2.imread('/home/brenda/Escritorio/tmpps5tswcu.png')

image = cv2.imread('/home/brenda/Escritorio/tmp47s462az.png')

print("imagen: ", image.shape, " ",  image.shape[0]* image.shape[1])

#row, columns X,Y
cv2.circle(image, (57, 96), 5, (0, 255, 0))
cv2.circle(image, (152, 169), 5, (0, 0, 255))
cv2.circle(image, (217, 141), 5, (255, 0, 0))
cv2.circle(image, (264, 120), 5, (255, 0, 0))
cv2.circle(image, (125, 84), 5, (255, 0, 0))


pixel_center1 = 76800 - ((96 * 320) +  57)
pixel_center2 = 76800 - ((169 * 320) +  152)
pixel_center3 = 76800 - ((141 * 320) +  217)
pixel_center4 = 76800 - ((120 * 320) +  264)
pixel_center5 = 76800 - ((84 * 320) +  125)

#image[96][57] = [255, 116, 140] X Y
#image[169][152] = [255, 116, 140]
#image[141][217] = [255, 116, 140]
#image[120][264] = [255, 116, 140]
#image[84][125] = [255, 116, 140]



#w and h  column 124 row 84
#(3,5) would lie in column number 3 and row number 5.

#index = (84  *  w320) + 124
############ index = (row * width) + column //// 122 * 320 + 245
#320 es largo
#primero ancho y luego alto

#guardado como 245 (ancho. col), 122 (alto, row)

#pixel_center = (obj["pixel_coords"][1] * height) + obj["pixel_coords"][0]

"""
pixel_center1 = (96 * 320) +  57
pixel_center2 = (169 * 320) +  152
pixel_center3 = (141 * 320) +  217
pixel_center4 = (120 * 320) +  264
pixel_center5 = (84 * 320) +  125
"""

"""
pixel_center1 = (96 * 240) +  57
pixel_center2 = (169 * 240) +  152
pixel_center3 = (141 * 240) +  217
pixel_center4 = (120 * 240) +  264
pixel_center5 = (84 * 240) +  125
"""
"""
pixel_center1 = (57  * 240) +  96
pixel_center2 = (152 * 240) +  169
pixel_center3 = (217 * 240) +  141
pixel_center4 = (264 * 240) +  120
pixel_center5 = (125 * 240) +  84

"""
"""
pixel_center1 = (57  * 320) +  96
pixel_center2 = (152 * 320) +  169
pixel_center3 = (217 * 320) +  141
pixel_center4 = (264 * 320) +  120
pixel_center5 = (125 * 320) +  84
"""

#print("center: ", pixel_center1)
#print("center: ", pixel_center2)
#print("center: ", pixel_center3)
#print("center: ", pixel_center4)
#print("center: ", pixel_center5)
#cv2.imshow('Test image', image)

# (3,3) 3,0 3,1 3,2 3,3 3,4
# (2,2) 2,0 2,1 2,2 2,3 2,4
# (1,1) 1,0 1,1 1,2 1,3 1,4
# (0,0) 0,0 0,1 0,2 0,3 0,4


#  0,0 0,1 0,2 0,3 0,4
#  1,0 1,1 1,2 1,3 1,4
#  2,0 2,1 2,2 2,3 2,4
#  3,0 3,1 3,2 3,3 3,4

#pixel_center = (args.width * args.height) - (obj["pixel_coords"][1] * args.width) + obj["pixel_coords"][0]
colores = {}

c = 0
r = 3
for i in range(20):
    if c >= 5:
        r -= 1
        c = 0
    print(r," --> ",c)
    c+=1


"""
counter = 0
for i, row in enumerate(image):
    # get the pixel values by iterating
    for j, pixel in enumerate(image):
        if counter == pixel_center1 or counter == pixel_center2 or counter == pixel_center3 or counter == pixel_center4:
            print("COLOR PINTADO", counter)
            image[i][j] = [255, 116, 140]
        counter += 1
"""


#print("COUNTER", counter)

'''
for i, row in enumerate(image):
    # get the pixel values by iterating
    for j, pixel in enumerate(image):
        if (i == j or i + j == image.shape[0]):
            #print("imprimir: ", list(image[i][j]))

            if (str(image[i][j][0])+"-"+str(image[i][j][1])+"-"+str(image[i][j][2])) in colores:
                colores[ (str(image[i][j][0])+"-"+str(image[i][j][1])+"-"+str(image[i][j][2]))  ] +=1
            else:
                colores[ (str(image[i][j][0])+"-"+str(image[i][j][1])+"-"+str(image[i][j][2]))  ] = 1
            # update the pixel value to black


for i, row in enumerate(image):
    # get the pixel values by iterating
    for j, pixel in enumerate(image):
        if (i == j or i + j == image.shape[0]):
            #print("imprimir: ", list(image[i][j]
            if (str(image[i][j][0])+"-"+str(image[i][j][1])+"-"+str(image[i][j][2])) == '64-64-64':
                image[i][j] = [255, 255, 0]
'''
cv2.imshow('Test image', image)

#170, 250
print(colores)

cv2.waitKey(0)
cv2.destroyAllWindows()



