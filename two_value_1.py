import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('huidu.png')
GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 中值滤波
GrayImage= cv2.medianBlur(GrayImage,5)
# GrayImage = cv2.bilateralFilter(GrayImage,9,75,75)
# GrayImage = cv2.GaussianBlur(GrayImage,(5,5),0)
# GrayImage = cv2.blur(GrayImage, (5,5))
ret,th1 = cv2.threshold(GrayImage,180,255,cv2.THRESH_BINARY)
# 3 为Block size, 5为param1值
# th2 = cv2.adaptiveThreshold(GrayImage,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#                     cv2.THRESH_BINARY,3,5)
# th3 = cv2.adaptiveThreshold(GrayImage,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#                     cv2.THRESH_BINARY,3,5)
# titles = ['Gray Image', 'Global Thresholding (v = 127)',
# 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
# images = [GrayImage, th1, th2, th3]
# for i in range(4):
#    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#    plt.title(titles[i])
#    plt.xticks([]),plt.yticks([])
# plt.show()
dst = cv2.dilate(th1, None, iterations=5)
dst = cv2.erode(dst, None, iterations=2)

cv2.imshow('GrayImage', GrayImage)
cv2.imshow('binary', dst)

cv2.waitKey(0)