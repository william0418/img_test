import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image

def his(b):
    img = Image.open(b)

    arr2 = np.array(img)

    M = arr2.shape[0]
    N = arr2.shape[1]
    arr2 = np.reshape(arr2,-1)

    plt.hist(arr2,bins = 256,range=(1, 256))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('title')

    plt.subplots_adjust(left=0.15)
    plt.show()
