import cv2
import numpy as np
import math


img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)

print(img.shape)

###################
#scaling
###################
rows, cols = img.shape

size = 2

img_output = np.zeros((img.shape[0]*size,img.shape[1]*size), dtype=img.dtype)

print(img_output.shape)

for i in range(rows):
    for j in range(cols):
        i_x = int(size*i)
        j_y = int(size*j)

        img_output[i_x,j_y] = img[i,j]

cv2.imshow('Input', img)
cv2.imshow('scaling', img_output)

########################
###ripple
##########################

img_output2 = np.zeros((img.shape[0]*size,img.shape[1]*size),dtype = img.dtype)

for i in range(rows):
    for j in range(cols):
        i_x = int(i+20*math.sin(2*math.pi*j/200))
        j_y = int(j+10*math.sin(2*math.pi*i/100))


        img_output2[i_x,j_y] = img[i,j]

cv2.imshow('Ripple', img_output2)
cv2.waitKey()
