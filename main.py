from histogram import his
from img_test import special_filters
import numpy as np

avg = 1./25
kernel = np.array([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])

special_filters('img.jpg',kernel=kernel,avg=avg)
