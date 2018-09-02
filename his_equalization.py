import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image

def his_equalization(b):
    img = Image.open(b)
    arr = np.array(img)
    arr = arr[:,:,1]
    print(arr)
    M = arr.shape[0]
    N = arr.shape[1]
    arr2 = np.reshape(arr,-1)

    max = arr2[np.argmax(arr2)]
    min = arr2[np.argmin(arr2)]
    arr = arr.astype(float)
    print(arr.dtype)

    
    for i in range(M):
        for j in range(N):
            if arr[i,j] > max:
                arr[i,j] = 255
            elif arr[i,j] < min:
                arr[i,j] = 0
            else :
                arr[i,j] = ((arr[i,j]-min)/(max-min))
    print(arr.dtype)

    plt.imshow(arr)
    plt.show()

    plt.hist(arr2,bins = 256,range=(1, 256))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('title')

    plt.subplots_adjust(left=0.15)
    plt.show()

his('gray.jpeg')
