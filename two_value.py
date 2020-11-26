import cv2

# 读取图像
img = cv2.imread('huidu.png')


# 均值滤波
# gray = cv2.blur(img, (5,5))

# 高斯滤波
# gray = cv2.GaussianBlur(img,(5,5),0)
#
# # 中值滤波
# gray = cv2.medianBlur(img, 5)
#
# # 双边滤波
# gray = cv2.bilateralFilter(img,9,75,75)

# 变微灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



# 大津法二值化
retval, dst = cv2.threshold(gray, 179, 255, cv2.THRESH_BINARY)



# 腐蚀和膨胀是对白色部分而言的，膨胀，白区域变大，最后的参数为迭代次数
# dst = cv2.dilate(dst, None, iterations=1)
# 腐蚀，白区域变小
# dst = cv2.erode(dst, None, iterations=1)

cv2.imshow('binary', dst)

cv2.waitKey(0)