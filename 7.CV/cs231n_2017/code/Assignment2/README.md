# Assignment #2: Fully-Connected Nets, Batch Normalization, Dropout,Convolutional Nets
## 1. 作业说明
2017年的作业二说明原链接：
+ md文件：<https://github.com/cs231n/cs231n.github.io/blob/master/assignments/2017/assignment2.md>
+ 网页：<https://cs231n.github.io/assignments2017/assignment2/>
+ 网页就是根据md显示的，所以二者内容完全相同，只是呈现形式不同

本次作业中，需要你练习写反向传播的代码，训练神经网络和卷积神经网络，目标如下：
+ 理解**神经网络**以及它们如何在层次结构中排列（堆叠顺序）
+ 理解并能够实现（向量化的）**反向传播**（ backpropagation）
+ 实现多种**更新规则**（update rules）来优化神经网络
+ 实现**BN**（batch normalization）用于神经网络的训练
+ 实现**dropout**来对网络进行正则化约束
+ 使用**交叉验证**（cross-validate）来高效的寻找神经网络架构的最优超参数
+ 了解**卷积神经网络**的架构，并通过在数据上训练这些模型获得训练网络的经验（例如：查看loss曲线调节lr参数等）

## 2. 设置
有两种完成作业的方式：
1. 本地运行
2. Google Cloud

Q5需要训练模型，所以建议使用有GPU的机器（需要配置NVIDIA Driver）

**作业2的文件压缩包在[这里](http://cs231n.stanford.edu/assignments/2017/spring1617_assignment2.zip)**
### 本地环境设置（同Assignment1）
下面以本地方式进行说明： 
+ **安装Python3.5+**
+ **建议使用虚拟环境(比如conda)**，至于完成作业需要使用的库，详见：`cs231n_2017/assignment/assignment1/requirements.txt`
    ```bash
    # 创建好虚拟环境后，切换到requirements.txt目录，执行以下命令即可
    pip install -r requirements.txt
    ```
### 数据下载（同Assignment1）
这里给出了脚本`cs231n_2017/assignment/assignment1/cs231n/datasets/get_datasets.sh`，脚本内容其实很简单，可以自己直接运行以下三个命令：
```bash
# Get CIFAR10
wget http://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
tar -xzvf cifar-10-python.tar.gz
rm cifar-10-python.tar.gz 
```

## 3. 作业文件说明
**Q：Question**
+ **Q1: Fully-connected Neural Network**（25分）， 在文件`FullyConnectedNets.ipynb`中，这个文件中介绍了模型层次结构设计以及使用这些层进行任意网络结构设计，并使用多种更新规则来优化模型
+ **Q2: Batch Normalization**(25分)，在文件`BatchNormalization.ipynb`中
+ **Q3: Dropout**（10分），在文件`Dropout.ipynb`中
+ **Q4: Convolutional Networks**(30分)，在文件`ConvolutionalNetworks.ipynb`中
+ **Q5: PyTorch / TensorFlow on CIFAR-10**(10分)，在文件`PyTorch.ipynb`或`TensorFlow.ipynb`中，任意选择其中一个完成，了解框架的使用并完全卷积神经网络的训练
+ **Q6: Cool Bonus: Do something extra!**(+10分)，额外探索，附加给10分

如果不想使用`jupyter`，在`cs231n_2017/assignment/assignment2/cs231n/classifiers`中也有对应的`.py`文件可以选择