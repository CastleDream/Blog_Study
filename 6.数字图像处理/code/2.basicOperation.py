# -*- encoding: utf-8 -*-
'''
@File    :   2.basicOperation.py
@Time    :   2023/05/31 11:04:28
@Author  :   huang shan 
@Version :   1.0
@Contact :   hs8023hfp@outlook.com
@License :   (C)Copyright 2023~
@Desc    :   None
'''
import pywt
import os
import SimpleITK as sitk
import numpy as np
import cv2
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei', 'Songti SC', 'STFangsong']
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['font.size'] = 8

path = "./6.数字图像处理/img"

singleDicomFilePath = os.path.join(
    path, "HIT-C12-cubePhantom/HITTest1Fld27.CT.Spezial_01HIT_.3.112.2012.03.23.10.48.59.159.25129945.dcm")
image = sitk.ReadImage(singleDicomFilePath)
image_np = sitk.GetArrayFromImage(image)

# -------------- 1. 添加随机噪声 ----------------#
plt.figure()
plt.subplot(2, 3, 1)
plt.imshow(image_np[0, :, :], cmap='gray')  # [0,512,512]的形状
plt.title("原图")

image_backUp = image_np.copy()
noise_np = np.zeros(image_np.shape)
for i in range(10):
    add_noise = np.random.uniform(0, 1, image_backUp.shape)
    image_backUp = image_backUp.astype(np.float64)+500*add_noise
    if i < 4:
        plt.subplot(2, 3, i+2)
        plt.title(f"添加了{i+1}次噪声的原图")
        plt.imshow(image_backUp[0, :, :], cmap='gray')
    noise_np = noise_np+add_noise
plt.subplot(2, 3, 6)
plt.title("添加10次噪声的结果")
plt.imshow(image_backUp[0, :, :], cmap='gray')
plt.show(block=True)

# ----------------2.傅里叶变换----------------#
# 使用傅里叶变换处理的只能是灰度图，所以读入的时候要注意转换

# 2.1 竖直条纹
image_path = os.path.join(path, "stripVertical.jpg")
image = cv2.imread(image_path)
image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.figure()

plt.subplot(3, 3, 1)
plt.title("原始图像")
plt.imshow(image[:, :, [2, 1, 0]])

plt.subplot(3, 3, 2)
plt.title("灰度图")
plt.imshow(image_grey, cmap="gray")

dft = np.fft.fft2(image_grey)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(np.abs(dft_shift))
"""
fft2生成的频谱, 低频在四个角
因此使用fftshift把高频分量放到四个角上, 把低频分量移动到图像中心
dft_shift生成的频谱是一个复数的量, 因此使用abs来取模, 同时由于频谱的模动态范围较大, 因此使用了log(压缩动态范围，便于肉眼观察)
magnitude_spectrum(振幅, 谱/频谱）
由于选择的图是纵向条纹衬衫,所以这些纵向条纹在横向上就形成了周期性的灰度变化(横向上很强的频率分量,横向上高频)
"""
plt.subplot(3, 3, 3)
plt.title("magnitude spectrum(频谱)")
plt.imshow(magnitude_spectrum, cmap='gray')
"""
频谱中心都是亮的:不管是什么图像, 肯定都存在大量的均匀区域（背景/低频),这个均匀区域对应着0频域的分量,0频域分量的能量很大
               也就是fftshift的函数说明中: Shift the zero-frequency component to the center of the spectrum.
横轴上, 有两个对称的亮点, 这两个对称的亮点就是衬衫上条纹在横向上周期性变化的频域
"""

# 2.1 水平条纹
image_h_path = os.path.join(path, "stripHorizen.jpg")
image_h_grey = cv2.imread(image_h_path, cv2.IMREAD_GRAYSCALE)
image_h = cv2.imread(image_h_path)

plt.subplot(3, 3, 4)
plt.title("原始图像")
plt.imshow(image_h[:, :, [2, 1, 0]])

plt.subplot(3, 3, 5)
plt.title("灰度图")
plt.imshow(image_h_grey, cmap="gray")

dft_h = np.fft.fft2(image_h_grey)
dft_shift_h = np.fft.fftshift(dft_h)
magnitude_spectrum_h = 20*np.log(np.abs(dft_shift_h))

plt.subplot(3, 3, 6)
plt.title("magnitude spectrum(频谱)")
plt.imshow(magnitude_spectrum_h, cmap='gray')
"""
这里的水平条纹和上面的竖直条纹,是类似的
水平条纹:则在竖直方向上会有周期性的灰度变化,因此,中心还是亮的,但是是竖直方向上有对称的亮点
倾斜方向也有一些亮度,这是因为这个图也存在一些斜着的条纹
"""
# 2.3 对竖直条纹旋转30°,查看频谱变化


def rotate_image(image, angle):
    col, row = image.shape[:2]
    M = cv2.getRotationMatrix2D(((col-1)/2.0, (row-1)/2.0), angle, 1)
    dst = cv2.warpAffine(image, M, (col, row),
                         flags=cv2.INTER_LINEAR, borderValue=255)
    # 不加borderValue=255,默认值是0,旋转后插值多出来的部分就是黑色(白色背景的图就要设置255)
    return dst


image_rotate = rotate_image(image_grey, 30)

plt.subplot(3, 3, 7)
plt.title("原图")
plt.imshow(image_grey, "gray")

plt.subplot(3, 3, 8)
plt.title("原图旋转30°")
plt.imshow(image_rotate, "gray")

dft_rotate = np.fft.fft2(image_rotate)
dft_shift_rotate = np.fft.fftshift(dft_rotate)
magnitude_spectrum_rotate = 20*np.log(np.abs(dft_shift_rotate))

plt.subplot(3, 3, 9)
plt.title("旋转30°对应的频谱")
plt.imshow(magnitude_spectrum_rotate, "gray")
"""
由于竖直条纹旋转了,之前水平方向上的灰度变化就变成倾斜方向的灰度周期性变化了,因此频谱也变成斜的了
"""
plt.show()

# ----------------3. 常见插值算法----------------#
interpolation_path = os.path.join(path, "transformer.jpeg")
interpolation_image = cv2.imread(interpolation_path, cv2.IMREAD_GRAYSCALE)

height, width = interpolation_image.shape
# img = cv2.imread()   height, width, channels = img.shape
downSampling = cv2.resize(
    interpolation_image, (round(width/4), round(height/4)))

# dsize(cols,rows)
upSampling1 = cv2.resize(downSampling, (width, height),
                         interpolation=cv2.INTER_NEAREST)
upSampling2 = cv2.resize(downSampling, (width, height),
                         interpolation=cv2.INTER_LINEAR)  # opencv中的cv2.INTER_CUBIC值得就是bilinear interpolation
upSampling3 = cv2.resize(downSampling, (width, height),
                         interpolation=cv2.INTER_CUBIC)  # opencv中的cv2.INTER_CUBIC指的就是bicubic interpolation
plt.figure()

plt.subplot(2, 3, 1)
plt.title("原图")
plt.imshow(interpolation_image, "gray")

plt.subplot(2, 3, 2)
plt.title("降采样为原始的1/4")
plt.imshow(downSampling, "gray")

plt.subplot(2, 3, 3)
plt.title("最近邻插值(cv2.INTER_NEAREST)")
plt.imshow(upSampling1, "gray")

plt.subplot(2, 3, 4)
plt.title("双线性插值(cv2.INTER_LINEAR)")
plt.imshow(upSampling2, "gray")

plt.subplot(2, 3, 5)
plt.title("双三次插值(cv2.INTER_CUBIC)")
plt.imshow(upSampling3, "gray")
# 一般双三次>双线性>最近邻,但是视觉上双三次和双线性基本看不出来,所以最常用的就是这两种插值方法,最近邻很少用
plt.show()

# ----------------4. 小波变换----------------#
singleDicomFilePath = os.path.join(
    path, "HIT-C12-cubePhantom/HITTest1Fld27.CT.Spezial_01HIT_.3.112.2012.03.23.10.48.59.159.25129945.dcm")
dicom_image = sitk.ReadImage(singleDicomFilePath)
dicom_np = np.squeeze(sitk.GetArrayFromImage(dicom_image))
cA, (cH, cV, cD) = pywt.dwt2(dicom_np, "db1")

AH = np.concatenate([cA, cH], axis=1)
VD = np.concatenate([cV, cD], axis=1)
img = np.concatenate([AH, VD], axis=0)

plt.figure()
plt.imshow(img, cmap='gray')
plt.show()
"""
cA左上角原图(其实是低频信息,可以理解为对原图进行降采样的结果)
cH右上角(水平方向上的高频)
cV左下角(竖直方向上的高频)
cD右下角(倾斜方向上的高频)
"""
