import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as Image
img = Image.open('img.jpg')
print(img.size)
arr_o = np.array(img)


##############################
#padding
##############################
kernel_size = 5
padding = 2

new_size = (img.size[0]+padding, img.size[1]+padding)
new_im = Image.new("RGB", new_size)

new_im.paste(img,(int((new_size[0]-img.size[0])/2),int((new_size[1]-img.size[1])/2)))

# new_im.show()


################################
#set the kernel
############################
avg = 1./25
kernel = np.array([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])
print(kernel)
###############################




M = new_im.size[0]
N = new_im.size[1]

arr = np.array(new_im)


########creat white image and put pixel in it#######
new_im2 = Image.new("RGB", img.size)
arr_new = np.array(new_im2)



#######converlution###########
for i in range(3):
    arr1 = arr[:, :, i]
    arr2 = arr_new[:,:,i]
    print(arr2.shape)
    for x in range(N-kernel_size):
    	for y in range(M-kernel_size):
            a = arr1[x:x+kernel_size, y:y+kernel_size]
            temp = np.sum(kernel*arr1[x:x+kernel_size, y:y+kernel_size])*avg
            # if temp < 0:
            #     temp = 0
            # elif temp > 255:
            #     temp = 255
            arr2[x, y] = int(temp)

    arr_new[:,:,i] = arr2
# arr_new = arr_new + arr_o
plt.imshow(arr_new)
plt.show()

############################




'''
print(arr[1][1].dtype)

arr1 = np.matrix([[1],[1],[1]])

arr3 = np.matrix([0.3333,0.3333,0.3333])

print(arr1.size)

arr2 = arr[1,1]*arr1

print(arr2)

arr2 = arr2*arr3

print(arr2)
'''



########turn to gray scale#######
arr = np.array([0.3333,0.3333,0.3333])
for i in range(img.size[1]):
    for j in range(img.size[0]):
        arr_o[i][j] = np.matmul(arr_o[i][j],arr)


print (arr_o[1][1])

#f = np.matmul(f,[0,0,0])

plt.imshow(arr_o)
plt.show()
