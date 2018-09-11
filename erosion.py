import cv2
import numpy as np

img = cv2.imread('j.png',0)
print(img)
kernel = np.ones((5,5),np.uint8)
kernel2 = np.array([[0, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0],
                   [0, 1, 1, 1, 0],
                   [0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0]], dtype=np.uint8)
print(kernel)
erosion = cv2.erode(img,kernel,iterations = 1)
erosion2 = cv2.erode(erosion,kernel2,iterations = 1)
dilation = cv2.dilate(img,kernel2,iterations = 1)


# for i in range(3):
#     erosion = cv2.erode(erosion,kernel2,iterations = 1)



cv2.imshow('erosion',erosion)
cv2.imshow('erosion2',erosion2)
cv2.imshow('dilation',dilation)
cv2.imshow(' boundary extraction',(dilation-img))
cv2.waitKey()
