# -*- encoding: utf-8 -*-
'''
@File    :   overview.py
@Time    :   2023/05/28 21:31:20
@Author  :   huang shan 
@Version :   1.0
@Contact :   hs8023hfp@outlook.com
@License :   (C)Copyright 2023~
@Desc    :   None
'''
from PIL import Image
import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# 注意，如果是使用vscode基于脚本运行，这里的路径是相对于执行目录的，所以要把执行目录切换到`6.数字图像处理`这一级
path = "./6.数字图像处理/img"

# ------------ 1. 压缩并保存不同质量图像 --------------#
srcImgPath = os.path.join(path, "zipQuality.jpg")
srcImg = cv2.imread(srcImgPath)

quality = 50
compressImagePath = os.path.join(path, "compress"+str(quality)+".jpg")
cv2.imwrite(compressImagePath, srcImg, [cv2.IMWRITE_JPEG_QUALITY, quality])

plt.figure()
plt.imshow(srcImg[:, :, [2, 1, 0]])
plt.show(block=True)

# ---------- 2.查看3通道直方图 --------------------#
colors = ("b", "g", "r")  # opencv的默认三通道顺序

plt.figure("histograms")
grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
plt.subplot(grid[0, 0:])
plt.title("src Image")
plt.imshow(srcImg[:, :, [2, 1, 0]])

for i, color in enumerate(colors):
    hist = cv2.calcHist([srcImg], [i], None, [256], [0, 255])
    plt.subplot(grid[1, i])
    plt.title(color+" channel")
    plt.plot(hist, color)
    plt.xlim([0, 256])
plt.show(block=True)

"""
对于示例图像,zipQuality.jpg,它的三通道直方图最高频位置对应的值是(200,200,100),
在图像窗口滑动一下,草地部分的值刚好对应这个高频颜色
"""

# --------3.色彩空间转换 ---------------------#
hsv = cv2.cvtColor(srcImg, cv2.COLOR_BGR2HSV)

# opencv显示
"""
hue,saturation,intensity = cv2.split(hsv)
# hue 即hsv[:,:,0]， saturation即hsv[:,:,1]， intensity即hsv[:,:,2]
HoriCom = np.concatenate((hue,saturation,intensity), axis=1)
cv2.imshow('h,s,v', HoriCom)
# 垂直或水平拼接，一次显示多图，参考https://www.geeksforgeeks.org/how-to-display-multiple-images-in-one-window-using-opencv-python/#

hueColor = cv2.applyColorMap(hue, cv2.COLORMAP_HSV)
cv2.imshow('hue', hueColor,)
cv2.imshow('saturation', saturation)
cv2.imshow('intensity', intensity)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
# matplotlib显示
colors = ("h", "s", "v")  # 色度，饱和度，亮度
plt.subplot(2, 2, 1)
plt.imshow(srcImg[:, :, [2, 1, 0]])

plt.subplot(2, 2, 2)
plt.title("hue channel")
plt.imshow(hsv[:, :, 0], cmap='hsv', interpolation="bicubic")

plt.subplot(2, 2, 3)
plt.title("saturation channel")
plt.imshow(hsv[:, :, 1], cmap='gray')

plt.subplot(2, 2, 4)
plt.title("intensity channel")
plt.imshow(hsv[:, :, 2], cmap='gray')

plt.show(block=True)


# ------------4.查看BGR三通道-----------------#
# opencv显示
# blue,green,red = cv2.split(srcImg)
# Hori = np.concatenate((blue,green,red), axis=1)
# cv2.imshow('b,g,r', Hori)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# matplotlib显示
colors = ("b", "g", "r")  # 色度，饱和度，亮度
plt.subplot(2, 2, 1)
plt.imshow(srcImg[:, :, [2, 1, 0]])
for i, color in enumerate(colors):
    plt.subplot(2, 2, i+2)
    plt.title(color+" channel")
    plt.imshow(srcImg[:, :, i], 'gray')
plt.show(block=True)

# ---------5. 查看CMYK通道----------------#
"""
基于opencv和matplotlib的,
可以看看https://code.adonline.id.au/cmyk-in-python/
和https://stackoverflow.com/questions/60814081/how-to-convert-a-rgb-image-into-a-cmyk
"""
bgrdash = srcImg.astype(np.float)/255.

K = 1 - np.max(bgrdash, axis=2)
C = (1-bgrdash[..., 2] - K)/(1-K)
M = (1-bgrdash[..., 1] - K)/(1-K)
Y = (1-bgrdash[..., 0] - K)/(1-K)

CMYK = (np.dstack((C, M, Y, K)) * 255).astype(np.uint8)
channels = ('c', 'm', 'y', 'k')

# 不那么好的cmap显示
plt.figure("wrong CMYK")
for i, channel, colormap in zip(range(4), channels, ('Greens', 'RdPu', 'YlOrBr', 'gray')):
    plt.subplot(2, 2, i+1)
    plt.title(channel+" channel")
    plt.imshow(np.asarray(CMYK[:, :, i]), cmap=colormap)
    # 在k中，以前白色的脸已经变成了黑色（值为0），gray显示模式，值越小，越黑

# 自定义符合CMYK模式的cmap
plt.figure("right CMYK")
cyan_cmap = ListedColormap(["black", "cyan"])
magenta_cmap = ListedColormap(["black", "magenta"])
yellow_cmap = ListedColormap(["black", "yellow"])


plt.subplot(2, 2, 1)
plt.title("cyan")
plt.imshow(np.asarray(CMYK[:, :, 0]), cmap=cyan_cmap)

plt.subplot(2, 2, 2)
plt.title("magenta")
plt.imshow(np.asarray(CMYK[:, :, 1]), cmap=magenta_cmap)

plt.subplot(2, 2, 3)
plt.title("yellow")
plt.imshow(np.asarray(CMYK[:, :, 2]), cmap=yellow_cmap)

plt.subplot(2, 2, 4)
plt.title("black")
plt.imshow(np.asarray(CMYK[:, :, 3]), cmap="gray")

plt.show(block=True)

# 基于PIL实现的（有点不符合实际情况）
"""
image = Image.open(srcImgPath)
# if image.mode == 'CMYK':
#     rgb_image = image.convert('RGB')
cmyk_image = image.convert('CMYK')

cmykTuple = cmyk_image.split()
channels = ('c', 'm', 'y', 'k')
for i, channel in enumerate(channels):
    plt.subplot(2, 2, i+1)
    plt.title(channel+" channel")
    plt.imshow(np.asarray(cmykTuple[i]), cmap='gray')

# 如果追求更好的颜色展示效果，可以
c, m, y, k = cmyk_image.split()
cmykTuple = cmyk_image.split()
channels = ('c', 'm', 'y', 'k')  # cyan(青色) magenta(品红) yellow black
plt.figure()
for i, channel, colormap in zip(range(4), channels, ('Greens', 'RdPu', 'YlOrBr', 'Greys')):
    plt.subplot(2, 2, i+1)
    plt.title(channel+" channel")
    plt.imshow(np.asarray(cmykTuple[i]), cmap=colormap)
plt.show(block=True)
"""
