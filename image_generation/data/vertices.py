import cv2
import numpy as np


path = "/home/brenda/Documents/master/semestre3/independent_study/clevr-dataset-generation-mask/output/images/CLEVR_new_000200_mask.png"
filename = 'env.jpg'

img = cv2.imread(path)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)    #--- convert to grayscale
bi = cv2.bilateralFilter(gray, 5, 75, 75)
cv2.imshow('bi',bi)

dst = cv2.cornerHarris(bi, 2, 3, 0.04)

#--- create a black image to see where those corners occur ---
mask = np.zeros_like(gray)

#--- applying a threshold and turning those pixels above the threshold to white ---
mask[dst>0.05*dst.max()] = 255
cv2.imshow('mask', mask)

img[dst > 0.01 * dst.max()] = [0, 0, 255]   #--- [0, 0, 255] --> Red ---
cv2.imshow('dst', img)

cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()