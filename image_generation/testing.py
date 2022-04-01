import random, cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt

pistas =   [[104, 263], [105, 254], [106, 245], [107, 236],
            [108, 228], [109, 224], [111, 222], [128, 222],
            [154, 224], [157, 226], [160, 228], [162, 230], [165, 232], [167, 234],
            [170, 236], [172, 238], [172, 245], [171, 252], [170, 259], [169, 265],
            [168, 272], [167, 279], [166, 282], [164, 284], [128, 286], [121, 286],
            [117, 284], [115, 281], [113, 279], [111, 276], [109, 274], [107, 271],
            [105, 269], [104, 267]]


filename ="/home/brenda/Downloads/balloon_dataset/balloon/train/34020010494_e5cb88e1c4_k.jpg"
window_name = 'image'

img = cv2.imread(filename)
height, width = img.shape[:2]
pistass = [[1020, 963],
            [1000, 899],
            [994, 841],
            [1003, 787],
            [1023, 738],
            [1050, 700],
            [1089,663],
            [1134, 638],
            [1190, 621],
            [1265, 619],
            [1321, 643],
            [1361, 672],
            [1403, 720],
            [1428, 765],
            [1442, 800],
            [1445, 860],
            [1441, 896],
            [1427, 942],
            [1400, 990],
            [1361, 1035],
            [1316, 1079],
            [1269, 1112],
            [1228, 1129],
            [1198, 1134],
            [1207, 1144],
            [1210, 1153],
            [1190, 1166],
            [1177, 1166],
            [1172, 1150],
            [1174, 1136],
            [1170, 1129],
            [1153, 1122],
            [1127, 1112],
            [1104, 1084],
            [1061, 1037],
            [1032, 989],
            [1020, 963]]
height = 440
width = 520
temp_colored_img = np.ones((height, width, 3))

for p in pistas:
    #print(p)
    temp_colored_img[p[0], p[1]] = [0, 0, 0]
    print(temp_colored_img[p[0], p[1]])


plt.imshow(temp_colored_img, interpolation='none')
plt.show()

#cv2.namedWindow('window_name', cv2.WINDOW_NORMAL)

#cv2.imshow("window_name", temp_colored_img) #.
# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
#cv2.waitKey(0)

# closing all open windows
#cv2.destroyAllWindows()