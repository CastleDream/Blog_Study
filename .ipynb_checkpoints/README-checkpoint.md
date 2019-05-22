# jupyter notebook 支持.md文件

参考链接：<br>
+ https://zh.d2l.ai/chapter_appendix/jupyter.html
+ https://www.jianshu.com/p/bda072a8587c
___

1. 首先，安装相应的包：<br>
>pip install https://github.com/mli/notedown/tarball/master

2. 打开jupyter notebook并加载插件:<br>
>jupyter notebook --NotebookApp.contents_manager_class='notedown.NotedownContentsManager'
3. 如果想每次运行Jupyter记事本时默认开启notedown插件，可以参考下面的步骤。
    1. 首先，执行下面的命令生成Jupyter记事本配置文件（如果已经生成，可以跳过）：
     >jupyter notebook --generate-config
    2. 然后，将下面这一行加入到Jupyter记事本配置文件（一般在用户主目录下的隐藏文件夹(C://users/shanshan).jupyter中的jupyter_notebook_config.py）的末尾
    >c.NotebookApp.contents_manager_class = 'notedown.NotedownContentsManager'
    3.之后，只需要运行jupyter notebook命令即可默认开启notedown插件。
    
4. 快速上手markdown语法：<br>
  https://gist.github.com/billy3321/1001749662c370887c63bb30f26c9e6e

# Blog_Study
记录一些博客的学习

## Beining_Learning
主要参考 https://cnbeining.github.io/deep-learning-with-python-cn/
+ 其中datasets文件夹已经放入教程所需的数据集

___
**第1-6章**
  <br>文字叙述背景介绍类
___
**第7章**
  <br>使用keras开发神经网络，使用的是皮马人糖尿病数据集，二分类问题，建立一个基本模型，方便后续操作
___
**第8章**
+ 对网络进行效果测试
    + 使用keras进行自动验证  
     使用model.fit(validation_split参数进行验证)
    + 使用keras进行手动验证
     可以自己创建一个train_test_split函数，加入validation_data参数作为验证数据
    + 使用keras进行K折交叉验证
     使用K折验证，将数据分成K组，留下1组验证，其他数据用作训练，直到每种分发的性能一致。
     深度学习一般不用交叉验证，因为对算力要求太高。例如：K折的次数一般是5或者10折，每组都需要训练并验证，训练时间成倍上升。
     使用了Sckicit-learn的StraitifiedKFold类 
___
**第9章**
+ 使用scikit-learn封装Keras的模型
    + scikit—leran封装了KerasClassifier和KerasRegressor
+ 使用scikit-learn对Keras的模型进行交叉验证
+ 使用scikit-learn，利用网格搜索调整Keras模型的超参
___
**第10章**
  <br>鸢尾花数据集分类，三分类
___
**第11章**
  <br>声呐返回值分类
  + 使用scikit-learn的Pipeline，进行数据预处理，使用StandardScaler
  + 调整模型的拓扑和神经元
      + 缩小网络（减少层的神经元）
      + 扩大网络（增加一个隐层）
      
___
**第12章**
  <br>波士顿住房价格回归
  + 交叉验证
  + 预处理数据
  + 微调网络参数
      + 更深的模型（增加参数）
      + 更宽的模型（增加神经元个数）
___
**第13章**
  <br>用序列化保存模型
  + 使用HDF5格式保存模型（权重）
  + 使用JSON格式保存模型
  + 使用YAML格式保存模型
___
**第14章**
  <br>使用保存点保存最好的模型
  + 使用保存点，ModelCheckpoint
  + 导入保存的模型（权重）
___
**第15章**
  <br>模型训练效果可视化
  + 使用history对象
  + 绘制acc/loss变化图像
___
**第16章**
  <br>使用dropout正则化防止过拟合
  + 使用dropout正则化的技巧
  (dropout原文给的一些建议)
___
**第17章**
  <br>学习速率设计
  + 按时间变化的学习速度调整
      keras内置了一个基于时间的学习速度调度器，按照训练轮数变化
  + 使用按训练次数变化的学习速度调整
      固定调度，到某个轮数就用某个速度。使用Keras的LearingRateScheduler作为回调参数可以控制学习速度，取当前轮数，返回应有的速度。
___



## TensorFlow_Tutoiral
主要参考 https://www.tensorflow.org/tutorials/keras/basic_classification
+ 目前只是实现了 Learn and use ML这个版块的，所使用的TensorFlow版本是1.13.1
+ 由于网速问题，直接在程序中load_data会报错，请求超时
+ 可以自己将load_data之后显示的download网址copy到迅雷下载，将下载的数据文件放入C盘下：./users/.keras/datasets中，这是默认的缓存目录，即可直接使用（由于Github上传文件大小限制，没有上传）

## 中国大学mooc学习
主要参考 https://www.icourse163.org/learn/NJU-1001571005?tid=1002097008#/learn/announce
+ 南京大学 张莉老师的 《用Python玩转数据》课程
+ 属于python数据处理的基础课程，适合入门

## 玉树芝兰
主要参考 https://www.jianshu.com/p/42ba125aa5dc
+ 简书上的一个叫 玉树芝兰 的博主 原名是 王树义 ，是某高校老师，教文科生做数据分析，所以教程相对浅显易懂，机器学习入门教程
+ 每个博文都是一个独立的教程，可以很快上手

## 深度框架学习

主要参考莫烦python的视频

## HATT实现

>使用的还是IMDB数据集。
+ 文件夹前面打对勾的表明是已经实现的，打×的是决定放弃的，打圈的是还有参考价值的。
+ HATT实现1是参考 https://github.com/richliao/textClassifier 这个我可以找到的star最多的层次注意力实现。
    + 后端使用Theano
+ HATT实现2是参考 https://github.com/indiejoseph/doc-han-att  这个有可视化的步骤 而且是中文的
    + 后端使用TensorFlow
    + ![img](https://github.com/indiejoseph/doc-han-att/raw/master/attention.png)
+ HATT实现3是参考 https://github.com/luisfredgs/cnn-hierarchical-network-for-document-classification 
    + 后端使用TensorFlow
+ HATT实现4是参考 https://github.com/Ashish-Gupta03/Hierarchical-Attention-Networks-for-Document-Classification-NAACL-2016
    + 后端使用TensorFlow
+ HATT实现5是参考 https://github.com/charlesdong1991/interpretable-han-for-document-classification-with-keras
    + TF后端
