# Assignment #3: Image Captioning with Vanilla RNNs, Image Captioning with LSTMs, Network Visualization, Style Transfer, Generative Adversarial Networks
## 1. 作业说明
2017年的作业三说明原链接：
+ md文件：<https://github.com/cs231n/cs231n.github.io/blob/master/assignments/2017/assignment3.md>
+ 网页：<https://cs231n.github.io/assignments2017/assignment3>
+ 网页就是根据md显示的，所以二者内容完全相同，只是呈现形式不同

本次作业中，你将实现RNN（循环神经网络，recurrent neural networks），同时在Microsoft COCO数据集上使用这个网络进行图像描述（image captioning）任务；也会探索ImageNet数据集上的预训练模型的特征图（features map）的可视化，并使用这个模型进行风格迁移（Style Transfer）；最后，会训练一个生成对抗(generative adversarial )网络来生成类似训练数据集的图像，目标如下：
+ 理解**recurrent neural networks** (RNNs) 的结构，以及它们如何在时间次数上通过共享权重来操作序列
+ 理解并实现普通的RNNs（普通循环神经网络，Vanilla RNNs）以及**LSTM RNNs**（LSTM循环神经网络）
+ 理解如何在**测试**时从RNN语言模型中采样
+ 理解如何组合CNN和RNN网络来实现一个**图像描述**系统
+ 理解一个训练好的CNN网络如何用于对输入图像进行**梯度计算**
+ 实现对图像梯度的不同应用，包括：saliency maps, fooling images, class visualizations
+ 理解并实现**风格迁移**
+ 理解如何训练一个**生成对抗网络**（GAN）来生成和数据集类似的图像


## 2. 设置
有两种完成作业的方式：
1. 本地运行
2. Google Cloud

GPU不是必须的，但是对于Question3~5来说，可以加速你的训练

**作业3的文件压缩包在[这里](http://cs231n.stanford.edu/assignments/2017/spring1617_assignment3_v3.zip)**
### 2.1 本地环境设置（同Assignment1）
下面以本地方式进行说明： 
+ **安装Python3.5+**
+ **建议使用虚拟环境(比如conda)**，至于完成作业需要使用的库，详见：`cs231n_2017/assignment/assignment1/requirements.txt`
    ```bash
    # 创建好虚拟环境后，切换到requirements.txt目录，执行以下命令即可
    pip install -r requirements.txt
    ```
### 2.2 数据下载
这里给出了脚本`7.CV/cs231n_2017/assignment/assignment3/cs231n/datasets/get_assignment3_data.sh`，脚本分别运行了三个数据集
```bash
#!/bin/bash
# 1. coco图像描述数据集下载
./get_coco_captioning.sh

wget "http://cs231n.stanford.edu/coco_captioning.zip"
unzip coco_captioning.zip
rm coco_captioning.zip

# 2. TensorFlow压缩模型下载
./get_squeezenet_tf.sh

wget "http://cs231n.stanford.edu/squeezenet_tf.zip"
unzip squeezenet_tf.zip
rm squeezenet_tf.zip

# 3. Imagenet验证集下载
./get_imagenet_val.sh

wget http://cs231n.stanford.edu/imagenet_val_25.npz
```

## 3. 作业文件说明
**Q：Question**，Questions 3~5都有pytorch和TensorFlow两个版本，自由选择
+ **Q1: Image Captioning with Vanilla RNNs**（25分）， 在文件`RNN_Captioning.ipynb`中
+ **Q2: Image Captioning with LSTMs**(25分)，在文件`LSTM_Captioning.ipynb`中
+ **Q3: Network Visualization: Saliency maps, Class Visualization, and Fooling Images**（15分），在文件`NetworkVisualization-TensorFlow.ipynb /NetworkVisualization-PyTorch.ipynb`中
+ **Q4: Style Transfer**(15分)，在文件`StyleTransfer-TensorFlow.ipynb/StyleTransfer-PyTorch.ipynb`中
+ **Q5: Generative Adversarial Networks**(10分)，在文件`GANs-TensorFlow.ipynb/GANs-PyTorch.ipynb`中
+ 没有额外作业奖励。

如果不想使用`jupyter`，在`cs231n_2017/assignment/assignment3/cs231n/classifiers`中也有对应的`.py`文件可以选择