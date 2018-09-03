import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image

def gray(b):
    img = Image.open(b)
    print(img.size)
    arr_o = np.array(img)

    arr = np.array([0.3333,0.3333,0.3333])
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            arr_o[i][j] = np.matmul(arr_o[i][j],arr)

    print (arr_o[1][1])
    return arr_o
    plt.imshow(arr_o)
    plt.show()




#######################################################

image = gray('gray.jpg')

for i in range(3):
    for j in range(image.shape[0]):
        for k in range(image.shape[1]):
            if image[j,k,i] < 128:
                image[j,k,i]=0
            else:
                image[j,k,i]=255


print(image)

plt.imshow(image)
plt.show()
