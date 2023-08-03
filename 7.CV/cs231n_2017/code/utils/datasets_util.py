# -*- encoding: utf-8 -*-
'''
@File    :   datasets_util.py
@Time    :   2023/08/03 15:41:36
@Author  :   huang shan 
@Version :   1.0
@Contact :   hs8023hfp@outlook.com
@License :   (C)Copyright 2023~
@Desc    :   None

https://github.com/keras-team/keras/blob/master/keras/datasets/cifar10.py
or pytorch
https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html
https://github.com/keras-team/keras/blob/master/keras/datasets/cifar10.py
'''

import numpy as np
import pickle
import os
import matplotlib.pyplot as plt
import cv2
plt.rcParams['font.sans-serif'] = ['SimHei', 'Songti SC', 'STFangsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 8


def unpickle(file):
    """
    Get data and labels numpy array dict
    Args:
    file: pickle file path
    Return:
    dict: which has data and labels key
    """
    with open(file, 'rb') as fo:
        # dict = pickle.load(fo, encoding='bytes')
        dict = pickle.load(fo, encoding='latin-1')
        # 参考：https://gist.github.com/KeitetsuWorks/52dba05742fe6b2e5313297dd9860d98
    return dict


def load_batch(file):
    """
    Get data and labels numpy array 
    Args:
    file: pickle file path
    Return:
    X: int8 numpy array, has been reshape to (sample_id,height,width,channel)
    Y: numpy array
    """
    pickleDict = unpickle(file)
    X = pickleDict['data']
    Y = pickleDict['labels']
    # must be np.uint8, if use np.int8, then image will has negative value and show wrong
    X = X.reshape(10000, 3, 32, 32).transpose(0, 2, 3, 1).astype(np.uint8)
    Y = np.array(Y)
    return X, Y


def load_cifar10(root):
    """
    load all cifar10 batch, including train and test datasets
    Args:
    file: cifar_10 root path
    Return:
    X_train,Y_train,X_test,Y_test
    """

    x_set = []
    y_set = []
    for batch_num in range(1, 6):
        filename = os.path.join(root, f"data_batch_{batch_num}")
        X, Y = load_batch(filename)
        x_set.append(X)
        y_set.append(Y)
    X_train = np.concatenate(x_set)
    Y_train = np.concatenate(y_set)
    X_test, Y_test = load_batch(os.path.join(root, "test_batch"))
    return X_train, Y_train, X_test, Y_test


def get_CIFAR10_data(train_num=49000, val_num=1000, test_num=10000, normalize=1):
    """
    Get Cifar10 data, split train datasets to train and validation, process normalize operation(subtract mean and divide std)
    Args:
    train_num: default is 49000
    val_num: default is 1000
    test_num: default is 10000
    normalize: int, default is 1.
            0 represent do not process normalize;
            1 represent process mean in image level; 
            2 represent process mean in channel level
    Return: dict, including train, val and test datasets
    {
      'X_train': X_train, 'y_train': y_train,
      'X_val': X_val, 'y_val': y_val,
      'X_test': X_test, 'y_test': y_test,
    }
    """
    root_path = "7.CV/cs231n_2017/datasets/cifar-10-batches-py"
    x_train, y_train, X_test, Y_test = load_cifar10(root_path)

    X_val = x_train[train_num:train_num+val_num]
    Y_val = y_train[train_num:train_num+val_num]
    X_train = x_train[:train_num]
    Y_train = y_train[:train_num]
    if normalize == 1:
        mean_image = np.mean(x_train, axis=0)
        std = np.std(x_train, axis=0)
        print(f"cifar10 mean_image is {mean_image.shape}")
        X_train -= mean_image
        X_val -= mean_image
        X_test -= mean_image
    if normalize == 2:
        # https://github.com/rishizek/tensorflow-deeplab-v3-plus/blob/master/utils/preprocessing.py#L49C65-L49C65
        # mean = []
        # std = []
        # for d in range(3):
        #     mean[d] += X[:, d, :, :].mean()
        #     std[d] += X[:, d, :, :].std()
        #     X_train[:,d,:,:] = (X_train[:,d,:,:] - means[d])/std[d]

        # x_train shape (10000,32,32,3)
        # https://github.com/CastleDream/d2l_learning/blob/master/d2l_zh_jupyter/self_exercise/28.%20BN%EF%BC%88%E6%89%B9%E9%87%8F%E5%BD%92%E4%B8%80%E5%8C%96%EF%BC%89.ipynb
        # https://stackoverflow.com/questions/47124143/mean-value-of-each-channel-of-several-images
        # https://bic-berkeley.github.io/psych-214-fall-2016/subtract_means.html
        # dim except channel, keepdims to guarantee subtract broadcasting
        mean = np.mean(X_train/255.0, axis=(0, 1, 2), keepdims=True)
        std = np.std(X_train/255.0, axis=(0, 1, 2), keepdims=True)
        print(
            f"cifar10 channel mean is {np.squeeze(mean)}, channel std is {np.squeeze(std)}")
        X_train = (X_train-mean)/std
        X_val = (X_val-mean)/std
        X_test = (X_test-mean)/std

    # transpose to guarantee channle first
    # np.transpose() just return a view of raw data, but not change the save order in memory, use copy() to change order in memory
    # https://stackoverflow.com/questions/19826262/transpose-array-and-actually-reorder-memory
    # https://numpy.org/doc/stable/reference/generated/numpy.transpose.html
    X_train = X_train.transpose(0, 3, 1, 2).copy()
    X_val = X_val.transpose(0, 3, 1, 2).copy()
    X_test = X_test.transpose(0, 3, 1, 2).copy()
    return {
        'X_train': X_train, 'Y_train': Y_train,
        'X_val': X_val, 'Y_val': Y_val,
        'X_test': X_test, 'Y_test': Y_test,
    }


if __name__ == "__main__":
    # test unpickle
    labels = unpickle(
        "7.CV/cs231n_2017/datasets/cifar-10-batches-py/batches.meta")["label_names"]
    print(labels)
    # ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

    # test load_batch
    test_batch = "7.CV/cs231n_2017/datasets/cifar-10-batches-py/data_batch_1"
    X, Y = load_batch(test_batch)
    print(X[1].shape, X[1][:, 1, 1])
    print(Y[1])
    # for i in range(25):
    #     plt.subplot(5, 5, i+1)
    #     plt.imshow(X[i])
    # plt.show()

    # test load_cifar10
    root_path = "7.CV/cs231n_2017/datasets/cifar-10-batches-py"
    x_train, y_train, x_test, y_test = load_cifar10(root_path)
    print(f"x_train shape: {x_train.shape},y_train shape: {y_train.shape} ")
    print(f"x_test shape: {x_test.shape},y_test shape: {y_test.shape} ")

    # test get_CIFAR10_data
    cifar10_data = get_CIFAR10_data(normalize=2)
    # cifar10 channel mean is [0.49131546 0.48209456 0.44646743], channel std is [0.2470337  0.2435103  0.26159205]
    # mean and std is same with https://stackoverflow.com/questions/66678052/how-to-calculate-the-mean-and-the-std-of-cifar10-data
