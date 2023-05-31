# -*- encoding: utf-8 -*-
'''
@File    :   1. medicalImageProcess.py
@Time    :   2023/05/30 10:59:12
@Author  :   huang shan 
@Version :   1.0
@Contact :   hs8023hfp@outlook.com
@License :   (C)Copyright 2023~
@Desc    :   None
'''
import pydicom
import SimpleITK as sitk
import os
import matplotlib.pyplot as plt

path = "./6.数字图像处理/img"

# --------- 1. 读取dicom图像，显示基本的meta信息 --------------#
reader = sitk.ImageFileReader()

singleDicomFilePath = os.path.join(
    path, "HIT-C12-cubePhantom/HITTest1Fld27.CT.Spezial_01HIT_.3.112.2012.03.23.10.48.59.159.25129945.dcm")
reader.SetFileName(singleDicomFilePath)
reader.LoadPrivateTagsOn()

reader.ReadImageInformation()

for k in reader.GetMetaDataKeys():
    v = reader.GetMetaData(k)
    # print(f'({k}) = = "{v}"')

print(f"Image Size: {reader.GetSize()}")
print(f"Image PixelType: {sitk.GetPixelIDValueAsString(reader.GetPixelID())}")

# --------- 2. 使用pydicom读取dicom图像，显示基本的meta信息 --------------#
dcmData = pydicom.read_file(singleDicomFilePath)
Modality = dcmData.Modality
Manufacturer = dcmData.Manufacturer
PixelSpacing = dcmData.PixelSpacing
XRayTubeCurrent = dcmData.XRayTubeCurrent
SliceThickness = dcmData.SliceThickness
print(f"Modality: {Modality}\nManufacturer: {Manufacturer}\nPixelSpacing: {PixelSpacing}\nXRayTubeCurrent:{XRayTubeCurrent}\n")
# print(dcmData.dir())

# --------- 3. 读取单个dicom图像，显示图像 -------------------#
image = sitk.ReadImage(singleDicomFilePath)
image_np = sitk.GetArrayFromImage(image)
plt.imshow(image_np[0, :, :], cmap='gray')
plt.show(block=True)
