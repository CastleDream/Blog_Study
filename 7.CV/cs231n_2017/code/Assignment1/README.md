# Assignment #1: Image Classification, kNN, SVM, Softmax, Neural Network
## 1. 作业说明
2017年的作业一说明原链接：
+ md文件：<https://github.com/cs231n/cs231n.github.io/blob/master/assignments/2017/assignment1.md>
+ 网页：<https://cs231n.github.io/assignments2017/assignment1/>
+ 网页就是根据md显示的，所以二者内容完全相同，只是呈现形式不同

本次作业中，需要你基于KNN（k-Nearest Neighbor）或者SVM/Softmax分类器完成一个简单的图像分类pipeline，目标如下：
+ 理解基本的**图像分类流程(Image Classification pipeline)**和**数据驱动方法（data-driven）**（训练/预测阶段）
+ 理解train/val/test的划分，以及使用验证集（val）进行超参微调的方法
+ 熟练使用numpy进行高效向量化编码
+ 实现并应用一个最近邻**KNN**(k-Nearest Neighbor)分类器
+ 实现并应用一个多类支持向量机**SVM**(Multiclass Support Vector Machine)分类器
+ 实现并应用一个**Softmax分类器**
+ 实现并应用一个**两层的神经网络**分类器
+ 理解这些分类器的差异以及优劣，作为使用时权衡的依据。
+ 对使用**更高级图像表示**而不是原始的像素带来的性能提升有一个基本的理解（例如：颜色直方图-color histograms, 梯度直方图-Histogram of Gradient (HOG) features）

## 2. 设置
有两种完成作业的方式：
1. 本地运行
2. Google Cloud

**作业1的文件压缩包在[这里](http://cs231n.stanford.edu/assignments/2017/spring1617_assignment1.zip)**
### 2.1 本地环境设置
下面以本地方式进行说明： 
+ **安装Python3.5+**
+ **建议使用虚拟环境(比如conda)**，至于完成作业需要使用的库，详见：`cs231n_2017/assignment/assignment1/requirements.txt`
    ```bash
    # 创建好虚拟环境后，切换到requirements.txt目录，执行以下命令即可
    pip install -r requirements.txt
    ```
### 2.2 数据下载
这里给出了脚本`cs231n_2017/assignment/assignment1/cs231n/datasets/get_datasets.sh`，脚本内容其实很简单，可以自己直接运行以下三个命令：
```bash
# Get CIFAR10
wget http://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
tar -xzvf cifar-10-python.tar.gz
rm cifar-10-python.tar.gz 
```

## 3. 作业文件说明
**Q：Question**
+ **Q1: k-Nearest Neighbor classifier**（20分）， 在文件`knn.ipynb`中
+ **Q2: Training a Support Vector Machine**(25分)，在文件`svm.ipynb`中
+ **Q3: Implement a Softmax classifier**（20分），在文件`softmax.ipynb`中
+ **Q4: Two-Layer Neural Network**(25分)，在文件`two_layer_net.ipynb`中
+ **Q5: Higher Level Representations: Image Features**(10分)，在文件`two_layer_net.ipynb`中
+ **Q6: Cool Bonus: Do something extra!**(+10分)，额外探索，附加给10分

如果不想使用`jupyter`，在`cs231n_2017/assignment/assignment1/cs231n/classifiers`中也有对应的`.py`文件可以选择