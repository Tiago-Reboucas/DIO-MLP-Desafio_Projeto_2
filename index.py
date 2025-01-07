import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

def rgb_to_gray(rgb_img):
    return np.dot(rgb_img[...,:3], [0.2989, 0.5870, 0.1140])

def read_img_src(gray_img):
    img_src = cv2.imread(gray_img)
    img_src = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
    return img_src

def gray_to_binarized(gray_img_matrix):
    black = 0
    white = 255
    thresh_value = 127

    initial_conversion = np.where((gray_img_matrix <= thresh_value), gray_img_matrix, white)
    final_conversion = np.where((initial_conversion > thresh_value), initial_conversion, black)

    return final_conversion


img = mpimg.imread('original.jpg')
gray = rgb_to_gray(img)
plt.imshow(gray, cmap=plt.get_cmap('gray'))
plt.show()
mpimg.imsave('gray.jpg', gray, cmap=plt.get_cmap('gray'))

input("\nPress Enter to continue:")
print()

binarized = gray_to_binarized(read_img_src("gray.jpg"))
plt.imshow(binarized, cmap=plt.get_cmap('gray'))
plt.show()
mpimg.imsave('binarized.jpg', binarized, cmap=plt.get_cmap('gray'))

input("\nPress Enter to continue:")
print()
