文件结构说明：
```bash
├── code
│   ├── 0.overview.py
│   ├── 1.medicalImageProcess.py
│   ├── test.ipynb
│   └── test.py
└── img
    ├── HIT-C12-cubePhantom 
    ├── building.jpg
    ├── cameraman.jpg
    ├── compress50.jpg
    ├── lenna.jpg
    |...
    └── zipQuality.jpg
```
0. overview.py
    1.压缩并保存不同质量图像
    2.查看3通道直方图
    3. hsv,cmyk颜色空间转换及对应通道显示，rgb通道显示
1. medicalImageProcess.py
    1. 读取dicom图像，显示基本的meta信息
    2. 读取单个dicom图像，显示图像
2. basicOperation.py
    1. 添加随机噪声
    2. 傅里叶变换，旋转
    3. 插值，resize
    4. 小波变换
+ HIT-C12-cubePhantom:
    + 医疗影像数据，来自https://github.com/SlicerRt/SlicerRtData/tree/master
    + 如果对别的有要求，也可以看看这个讨论：https://fluka-forum.web.cern.ch/t/publicly-available-dicom-files/2264
+ 其余数字图像处理相关的原图，都来自这个课程的[课程作业](https://ustc-dip.github.io/#courseware)