# Nâng cấp ảnh dùng Difference of Gaussian (DoG)
#https://theailearner.com/2019/05/13/difference-of-gaussians-dog/
import cv2
img = cv2.imread('test0.tif',0)
from matplotlib import pyplot as plt
 
# Apply 3x3 and 7x7 Gaussian blur
low_sigma = cv2.GaussianBlur(img,(3,3),0)
high_sigma = cv2.GaussianBlur(img,(5,5),0)
 
# Calculate the DoG by subtracting
dog = low_sigma - high_sigma

# Display
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(low_sigma,cmap = 'gray')
plt.title('Low Sigma'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(high_sigma,cmap = 'gray')
plt.title('High Sigma'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(dog,cmap = 'gray')
plt.title('Difference of Gaussian'), plt.xticks([]), plt.yticks([])
plt.show()

