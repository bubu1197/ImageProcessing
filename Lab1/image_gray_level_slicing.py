# 5. Cắt lát mức xám
import cv2
import matplotlib.pyplot as plt 
import math
import numpy as np

# Graylevel slicing with background

image=cv2.imread('dolar.tif',0)
x,y=image.shape
z=np.zeros((x,y))
for i in range(0,x):
    for j in range(0,y):
        if(image[i][j]>50 and image[i][j]<150):
            z[i][j]=255
        else:
            z[i][j]=image[i][j]
equ=np.hstack((image,z))
plt.title('Original\Graylevel slicing with background')
plt.imshow(equ,'gray')
plt.show()

# Graylevel slicing without background

z=np.zeros((x,y))
for i in range(0,x):
    for j in range(0,y):
        if(image[i][j]>50 and image[i][j]<150):
            z[i][j]=255
        else:
            z[i][j]=0
equ=np.hstack((image,z))
plt.title('Original\Graylevel slicing w/o background')
plt.imshow(equ,'gray')
plt.show()