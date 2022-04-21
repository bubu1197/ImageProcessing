# 2a - Làm mềm ảnh (blur/smoothing ) bằng lọc Gaussian
#https://thigiacmaytinh.com/lam-min-anh-smoothing/
#https://aicurious.io/posts/2018-09-29-loc-anh-image-filtering/
import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread('test0.tif',0)
 
# Averaging
blur = cv2.blur(img,(3,3))
 
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Averaging_blur')
plt.xticks([]), plt.yticks([])
plt.show()

# Gausian
GaussianBlur = cv2.GaussianBlur(img,(3,3),0)
 
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(GaussianBlur),plt.title('Gaussian_blur')
plt.xticks([]), plt.yticks([])
plt.show()

# Median 
median = cv2.medianBlur(img,5)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Median_blur')
plt.xticks([]), plt.yticks([])
plt.show()

# Bilateral Filtering: thích hợp để làm mịn như filter 

filter  = cv2.bilateralFilter(img,9,75,75)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(filter),plt.title('Bilateral Filtering_blur')
plt.xticks([]), plt.yticks([])
plt.show()


