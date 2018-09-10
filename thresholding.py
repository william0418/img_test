import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image
import cv2

def gray(b):
    img = cv2.imread(b)
    print(img.shape)
    arr_o = np.array(img)

    arr = np.array([0.3333,0.3333,0.3333])
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            arr_o[i][j] = np.matmul(arr_o[i][j],arr)

    print (arr_o[1][1])
    return arr_o




#######################################################

image = gray('img.jpg')

level = 150

for i in range(3):
    for j in range(image.shape[0]):
        for k in range(image.shape[1]):
            if image[j,k,i] < level:
                image[j,k,i]=0
            else:
                image[j,k,i]=255


cv2.imshow('thresholding', image)
cv2.waitKey()
