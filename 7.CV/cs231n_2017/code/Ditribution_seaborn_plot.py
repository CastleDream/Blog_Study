import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# <https://blog.csdn.net/Castlehe/article/details/127555925>
# 6. 正态(normal)/高斯(gaussian)分布distribution 3σ原则
# μ-σ~μ+σ=0.6826，（0-1~0+1   点落在-1~1之间的概率是68.26%）
# μ-2σ~μ+2σ=0.9544    (点落在-2~2之间的概率是95.44%）
# μ-3σ~μ+3σ=0.9974    (点落在-3~3之间的概率是99.74%）

x = np.random.randn(2000)
y = np.random.randn(2000)

# sns.jointplot(x=x, y=y, kind="reg")
# sns.jointplot(x=x, y=y, kind="kde")

# g = sns.jointplot(x=x, y=y)
# g.plot_joint(sns.kdeplot, color="r", zorder=0, levels=6) # 添加kde概率密度图显示
# plt.show()

fig = plt.figure()
gs = fig.add_gridspec(2, 2,  width_ratios=(4, 1), height_ratios=(1, 4),
                      left=0.1, right=0.9, bottom=0.1, top=0.9,
                      wspace=0.05, hspace=0.05)
ax = fig.add_subplot(gs[1, 0])
sns.scatterplot(x=x, y=y, ax=ax)

ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
sns.histplot(x=x, bins=10, ax=ax_histx)
ax_x2 = ax_histx.twinx()
sns.kdeplot(x=x, ax=ax_x2)


ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)
sns.histplot(y=y, bins=10, ax=ax_histy)
ax_y2 = ax_histy.twiny()
sns.kdeplot(y=y, ax=ax_y2)

plt.show()
