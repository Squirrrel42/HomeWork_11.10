from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage

img = Image.open('image.jpg')
img_arr = np.array(img)
height = img_arr.shape[0]
width = img_arr.shape[1]
if len(img_arr.shape) != 3:
    temp = np.empty((height, width, 3))
    temp[:, :, 0] = img_arr
    temp[:, :, 1] = img_arr
    temp[:, :, 2] = img_arr
    img_arr = temp

weight = np.random.random_sample(size=(10,10))

def blur(img_arr, weight):
    weight /= weight.sum()
    blur_arr_col = np.empty((height, width, 3))
    blur_arr = np.empty((height, width, 3))

    for i in range(3):
        blur_arr_col[:, :, i] = scipy.ndimage.convolve(img_arr[:, :, i], weight)
        blur_arr_col[:, :, i] = blur_arr_col[:, :, i]/blur_arr_col[:, :, i].max()

    for i in range(3):
        blur_arr[:, :, i] = blur_arr_col[:, :, i]



    return blur_arr


plt.imshow(blur(img_arr, gauss))
plt.show()