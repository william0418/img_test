import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image
import cv2

# def his_equalization(b):
#     arr = cv2.imread(b, cv2.IMREAD_GRAYSCALE)
#
#     cv2.imshow('input',arr)
#
#     arr_new = np.reshape(arr,-1)
#
    # plt.hist(arr_new,  bins = 256,  range=(1, 256))
    #
    # plt.show()


################################
###some problem :output is a green image
#################################
    # img = Image.open(b)
    # arr = np.array(img)
    # arr_new = np.zeros(arr.shape)
    # arr_new = arr[:,:,2]
    # plt.imshow(arr_new)
    # plt.show()
#######################################


    # M = arr.shape[0]
    # N = arr.shape[1]
    # arr2 = np.reshape(arr,-1)
    #
    # max = arr2[np.argmax(arr2)]
    # min = arr2[np.argmin(arr2)]
    # arr = arr.astype(float)
    # print(arr.dtype)
    #
    #
    #
    # # for i in range(arr2.shape[0]):
    # #     arr2[i] = ((max-arr2[i])/(max-min))*100
    #
    #
    # for i in range(M):
    #     for j in range(N):
    #         if arr[i,j] > max:
    #             arr[i,j] = 255
    #         elif arr[i,j] < min:
    #             arr[i,j] = 0
    #         else :
    #             # arr[i,j] = ((arr[i,j]-min)/(max-min))*255
    #             arr[i,j] = int(((max-arr[i,j])/(max-min))*255)
    # print(arr.dtype)
    #
    # plt.imshow(arr)
    # plt.show()
    #

    # plt.hist(arr2, bins = 256, range=(1, 256))
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.title('title')
    # plt.subplots_adjust(left=0.15)
    # plt.show()
    #
# his_equalization('img.jpg')

arr_o = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('input',arr_o)

arr_new = np.reshape(arr_o,-1)

arr_count = np.zeros((256,),dtype = int)
arr = arr_new
for i in range(arr_new.shape[0]):
    j = arr[i]
    arr_count[j]+=1


for i in range(1,256):
    arr_count[i] = arr_count[i]+arr_count[i-1]

all_pixel = arr_count[255]

for i in range(arr_o.shape[0]):
    for j in range(arr_o.shape[1]):
        a = arr_o[i,j]
        arr_o[i,j] = ((arr_count[a]-1)/all_pixel)*255

cv2.imshow('golble',arr_o)

###local

local_max = 100
local_min = 0


local_pixel = arr_count[local_max]-arr_count[local_min]

arr_local = arr_o.copy()

for i in range(arr_o.shape[0]):
    for j in range(arr_o.shape[1]):
        a = arr_local[i,j]
        if a >local_min-1 and a < local_max+1:
            arr_local[i,j] = ((arr_count[a]-arr_count[local_min])/(local_pixel-arr_count[local_min]))*(local_max-local_min)+local_min

cv2.imshow('local', arr_local)


cv2.waitKey()
