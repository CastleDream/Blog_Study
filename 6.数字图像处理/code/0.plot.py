import os
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei', 'Songti SC', 'STFangsong']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 12


# --------1. 绘制不同marker和线型、颜色 ------------
plt.figure(figsize=(10, 6))
# plt.margins(x=0)
plt.xticks(list(np.arange(0, 16, 1)))

markerList = [".", ",", "o", "v", "^", "<", ">", "1", "2", "3", "4", "8", "s", "p", "P",
              "*", "h", "H", "+", "x", "X", "D", "d", "|", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, '$f$']
lineList = ["-", '--', '-.', ':']
colorList = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'tab:cyan', 'tab:olive',
             'tab:gray', 'tab:pink', 'tab:brown', 'tab:purple', 'tab:red', 'tab:orange', 'tab:blue']

markerNum = len(markerList)
lineNum = len(lineList)
colorNum = len(colorList)
print(
    f"marker num is {markerNum}, line num is{lineNum}, color num is {colorNum}")

offset = 0
for index in range(0, markerNum, 3):
    # print(f"index is {index}")
    if (markerNum-index) >= 3:
        groupNum = 3
    else:
        groupNum = markerNum-index
        # print(f"groupNum = {groupNum}")
    for lineIndex in range(groupNum):
        outIndex = index+lineIndex
        # print(f"out index is {outIndex}")
        marker = markerList[outIndex]
        lineStyle = lineList[outIndex % lineNum]
        color = colorList[outIndex % colorNum]

        x = np.arange(5*lineIndex, 5*(lineIndex+1), 0.5)
        y = [0.1+offset]*5+[0.2+offset]+[0.1+offset]*4
        plt.plot(x, y, color=color, marker=marker, linestyle=lineStyle)
        if isinstance(marker, str):
            plt.text(x[0], y[0]+0.1, marker+lineStyle+color)
        else:
            plt.text(x[0], y[0]+0.1, "num_"+str(marker)+lineStyle+color)
            # print(f"outIndex = {outIndex}")
    offset += 0.5
# plt.legend()
plt.show()
