# -*- encoding: utf-8 -*-
'''
@File    :   3.greyLevelTransformation.py
@Time    :   2023/06/05 09:50:17
@Author  :   huang shan 
@Version :   1.0
@Contact :   hs8023hfp@outlook.com
@License :   (C)Copyright 2023~
@Desc    :   None
'''

import os
import matplotlib.pyplot as plt
import cv2
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei', 'Songti SC', 'STFangsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 8


path = "./6.数字图像处理/img"
snow_image_path = os.path.join(path, "snowHourse.jpeg")
snow_image = cv2.imread(snow_image_path, cv2.IMREAD_GRAYSCALE)  # 原图是彩色，以灰度图读入
print(f"输入图像的Shape(验证读入是灰度):{snow_image.shape}")

# --------- 0. 查看直方图 ------------
histogram = cv2.calcHist([snow_image], [0], None, [256], [0, 256])

"""
plt.figure() #这个和课程显示的直方图部分图像长宽比不太一样,看起来没那么方便
grid = plt.GridSpec(2, 2, wspace=0.4, hspace=0.3)

plt.subplot(grid[0, 0:])
plt.title("原图")
plt.imshow(snow_image, cmap='gray')

plt.subplot(grid[1, 0])
plt.title("cv+plot的histogram")
plt.yticks(range(0, 12000, 1000))
plt.plot(histogram)

plt.subplot(grid[1, 1])
plt.title("numpy+hist的histogram")
plt.hist(snow_image.ravel(), 256, [0, 256])
plt.show()
"""
plt.figure()
plt.subplot(1, 2, 1)
plt.title("原图")
plt.imshow(snow_image, cmap='gray')

plt.subplot(1, 2, 2)
# 我找的图像整体也比课上的要亮一些,所以没法做到完全一致
plt.hist(snow_image.ravel(), 256, [0, 256])

thresholdPoint = [0, 50, 180, 255]  # 以这四个点大概可以区分出亮区和暗区
plt.plot(thresholdPoint, histogram[thresholdPoint])
plt.show()

# --------- 1. 灰度线性变换 -----------
"""
直方图上可以大致选择出:暗区和灰区的分界点-(50,30);灰区和亮区的分界点-(180,120)
即(0,0)~(50,30)-暗区,(50,30)~(180,120)-灰区, (180,120)~(256,256)-亮区
横坐标是当前图像的灰度值, 纵坐标是变换后的灰度值
"""
plt.figure()
plt.plot([0, 50, 180, 256], [0, 30, 120, 256], "D-b", mfc='red', mec='k')
plt.show()

# --------- 2.直方图均衡化 ------------

# --------- 3.直方图规定化 ------------
