import numpy as np

x = np.array([[1,2],[3,4]])

b = np.array([32,74])

y = np.linalg.solve(x,b)

print(y)

#############################################
##i don't think the code can work!!!!!
###############################################

img = cv2.imread('', cv2.IMREAD_GRAYSCALE)

arr = np.zeros(2,(img.shape[0]+img.shape[1])*2)
arr_xy = np.zeros(5,(img.shape[0]+img.shape[1])*2)

for i in range(img.shape[0]):
    for j in range(im.shape[1]):
        if im[i,j] != 0:
            arr[0,i] = i
            arr[1,i] = j
            arr_xy[0,i] = 1
            arr_xy[1,i] = pow(arr[0,i],1)
            arr_xy[2,i] = pow(arr[0,i],2)
            arr_xy[3,i] = pow(arr[1,i],1)
            arr_xy[4,i] = pow(arr[1,i],2)
            arr_xy[5,i] = arr[0,i]*arr[1,i]
            break()

for i in range(img.shape[0]):
    for j in range(im.shape[1]):
        if im[i,im.shape[1]-j] != 0:
            arr[0,img.shape[0]+i] = i
            arr[1,img.shape[0]+i] = im.shape[1]-j
            break()

for j in range(img.shape[1]):
    for i in range(img.shape[0]):
        if im[i,j]!= 0:
            arr[0,2*img.shape[0]+j] = i
            arr[1,2*img.shape[0]+j] = j
            break()

for j in range(img.shape[1]):
    for i in range(img.shape[0]):
        if im[img.shape[0]-i,j]!= 0:
            arr[0,2*img.shape[0]+img.shape[1]+j] = img.shape[0]-i
            arr[1,2*img.shape[0]+img.shape[1]+j] = j
            break()
print(arr)
