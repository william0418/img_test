import numpy as np
import matplotlib.pyplot as plt
import PIL.Image as Image

####take the random point##########

arr = [np.array([1,2,3]),np.array([2,3,4])]
img = np.array([[248, 168,  58,   20,   100],
       [  80, 100,   32,   50, 101],
       [  20,   90, 106,   12,   80],
       [131,   202,   510,  90,   312],
       [  180, 100,   112,   510,  83]])

s = (20,20)
s = np.zeros(s)
coords = [np.random.randint(0, i - 1, 10) for i in img.shape]
print(coords)

img[coords] = 0

print(img)

##############create gaussian use in 3 chennel###############
image = Image.open('img.jpg')
image = np.array(image)

print(image.shape)

row,col,ch= image.shape
image.reshape(row,col*3)
mean = 0
var = 50
sigma = var**0.5
# gauss = np.random.normal(mean,sigma,(row,col,ch))
# gauss = gauss.reshape(row,col,ch)
# noisy = image + gauss

gauss = np.random.normal(mean,sigma,(row,col))
gauss = gauss.reshape(row,col)

image[:,:,0] = image[:,:,0] + gauss
image[:,:,1] = image[:,:,1] + gauss
image[:,:,2] = image[:,:,2] + gauss


print(gauss)
print('1111111111111111111111111111')
print(image)

plt.imshow(image)
plt.show()
