# Nâng cấp ảnh dùng Laplacian of Gaussian (LoG)
#https://theailearner.com/2019/05/25/laplacian-of-gaussian-log/#:~:text=Unlike%20first%2Dorder%20filters%20that,to%20positive%20and%20vice%2Dversa.
import cv2
import numpy as np
from matplotlib import pyplot as plt
 
# Load the image in greyscale
img = cv2.imread('test0.tif',0)
 
# Apply Gaussian Blur
blur = cv2.GaussianBlur(img,(3,3),0)
 
# Apply Laplacian operator in some higher datatype
laplacian = cv2.Laplacian(blur,cv2.CV_64F)

# But this tends to localize the edge towards the brighter side.
laplacian1 = laplacian/laplacian.max()

# Dispalay
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(blur,cmap = 'gray')
plt.title('Gaussian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(laplacian1,cmap = 'gray')
plt.title('Laplacian of Gaussian'), plt.xticks([]), plt.yticks([])
plt.show()

