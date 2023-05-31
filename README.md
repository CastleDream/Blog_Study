# 简介
这个repo主要存放之前学习过的一些内容

## 1. Beining_Learning
学习来源: <https://cnbeining.github.io/deep-learning-with-python-cn/>

文件结构说明:
```bash
├── 1. Beining_Learning
  ├── datasets //教程所需的数据集
  ├── dropout_paper.pdf
  ├── 第10章 鸢尾花分类.ipynb //鸢尾花数据集分类，三分类
  ├── 第11,16章 声呐返回值分类.ipynb //11.scikit-learn的Pipeline，进行数据预处理，使用StandardScaler,调整模型的拓扑和神经元；16. dropout正则化
  ├── 第12章 波士顿住房价格回归.ipynb //交叉验证，预处理，网络结构调整
  ├── 第17章 学习速率设计.ipynb //keras LearingRateScheduler，按照时间或训练轮数设置
  └── 第7,8,9,13,14,15章-皮马人糖尿病.ipynb //7.keras二分类网络；8.精度自动/手动验证（k折交叉验证）；9.基于scikit-learn的网格搜索；13.HDF5、Json、YAML等格式保存模型权重；14.保存点保存，导入；15.绘制loss、acc图像可视化训练效果
```
P.S.1-6章节，是文字叙述背景介绍类，

## 2.TensorFlow_Tutoiral
学习来源：<https://www.tensorflow.org/tutorials/keras/basic_classification>
+ (上面的网页已经404了，tf确实更新的很快啊)

文件结构说明：
```bash
.
├── 19-4-20-Tensorflow-Tutorials-衣服10分类.ipynb
├── 19-4-20-影评文本二分类.ipynb
├── 19-4-22-回归：预测燃油效率.ipynb
├── 19-4-23-关于过拟合和欠拟合-以IMDB数据集为例.ipynb
├── 19-4-24-保存和恢复模型.ipynb
```

如果网速有问题，无法使用load_data，则可以自己预先下载好，放到对应文件夹下。
1. 查看mnist.load_data()所在的.py文件，可以知道本地缓存地址在~./keras/datasets
    ```python
    https://www.tensorflow.org/api_docs/python/tf/keras/datasets/mnist/load_data
    tf.keras.datasets.mnist.load_data(path='mnist.npz')
    Defined in tensorflow/python/keras/datasets/mnist.py.
    Loads the MNIST dataset.
    Arguments:
    path: path where to cache the dataset locally (relative to ~/.keras/datasets).
    ```
2. 在jupyter里下载的，所以找到`C:\Users\yourname\.keras\datasets`
看到之前下载的缓存，将fashion_mnist的放到文件夹里

## 3.用Python玩转数据
学习来源：<https://www.icourse163.org/learn/NJU-1001571005?tid=1002097008#/learn/announce>
+ 南京大学 张莉老师的 《用Python玩转数据》课程
+ 属于python数据处理的基础课程，适合入门
+ 有一个简单的爬取豆瓣书评的示例

## 4. 玉树芝兰
学习来源：<https://www.jianshu.com/p/42ba125aa5dc>
+ 简书上的一个叫 玉树芝兰 的博主 原名是 王树义 ，是某高校老师，教文科生做数据分析，所以教程相对浅显易懂，机器学习入门教程
+ 每个博文都是一个独立的教程，可以很快上手

文件结构说明：
```bash
.
├── DecisionTree
├── SVM
├── Topic_extract
├── 舆情时间序列分析
├── 对故事情节做情绪分析
├── 提取中文长文档关键字
├── 训练自己的情感分类模型
└── 深度学习分类即将流失客户tflearn
```

## 5.graphviz使用
graphviz学习的相关参考和练习

## 6. 数字图像处理
学习来源：
+ 测试图像和主要代码：<https://ustc-dip.github.io/#courseware>
+ 视频和部分代码：<https://www.icourse163.org/course/DUT-1002014037?tid=1467299448>

文件结构说明：
```bash
```
## drawio_save
存放使用drawio绘制的图形的源文件