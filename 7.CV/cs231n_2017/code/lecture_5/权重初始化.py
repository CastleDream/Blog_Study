import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(threshold=8, suppress=True)

D = np.random.randn(1000, 500)
hidden_layer_sizes = [500]*10  # [500,500,500,...500], 10个500的列表
# X           W        Y
# 1000*500    500*10   1000*10
# 如果画成图，输入层就是500个圈圈，第一个隐藏层就是10个圈圈，之间权重连线的个数是500*10
nonlinearities = ['tanh']*len(hidden_layer_sizes)
# nonlinearities = ['relu']*len(hidden_layer_sizes)

act = {"relu": lambda x: np.maximum(0, x), "tanh": lambda x: np.tanh(x)}
Hs = {}

for i in range(len(hidden_layer_sizes)):
    X = D if i == 0 else Hs[i-1]
    fan_in = X.shape[1]
    fan_out = hidden_layer_sizes[i]
    # Xavier initialization
    W = np.random.randn(fan_in, fan_out) * np.sqrt(2/1000)
    # W = np.random.randn(fan_in, fan_out) / np.sqrt(fan_in)
    # W = np.random.randn(fan_in, fan_out)*0.01  # small stable
    # W = np.random.randn(fan_in, fan_out)  # small stable

    H = np.dot(X, W)  # 输出1000*10
    # 隐式函数/动态构建函数 https://www.cnblogs.com/fireblackman/p/16192027.html
    H = act[nonlinearities[i]](H)
    Hs[i] = H


print(f"Input layer had mean: {np.mean(D)}, std: {np.std(D)}")
layers_means = [np.mean(H) for i, H in Hs.items()]
layers_stds = [np.std(H) for i, H in Hs.items()]
for key, value in Hs.items():
    print(
        f"Hidden layer {key+1} had mean: {layers_means[key]:{1}.{5}}, std: {layers_stds[key]:{0}.{5}}")

plt.figure()
plt.subplot(121)
plt.plot(Hs.keys(), layers_means, 'ob-')
plt.title("Layer mean")

plt.subplot(122)
plt.plot(Hs.keys(), layers_stds, 'or-')
plt.title("Layer std")

plt.figure()
for key, value in Hs.items():
    # 1000*10（经过了激活函数的输出y）拉平后，1w个数字里，tanh的话，值属于[-1,1]的频率直方图
    plt.subplot(1, len(Hs), key+1)
    plt.hist(value.ravel(), 30, range=(-1, 1))
plt.show()
