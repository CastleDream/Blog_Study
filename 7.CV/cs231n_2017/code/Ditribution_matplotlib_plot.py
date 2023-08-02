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
z = np.random.randn(2000)

# ------------- matplotlib -----------------
# 3D
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(x, y, z, marker='o', c='blue')

h, yedges, zedges = np.histogram2d(y, z, bins=50)
h = h.transpose()
normalized_map = plt.cm.Blues(h/h.max())

yy, zz = np.meshgrid(yedges, zedges)
xpos = min(x)-2  # Plane of histogram
xflat = np.full_like(yy, xpos)

p = ax.plot_surface(xflat, yy, zz, facecolors=normalized_map,
                    rstride=1, cstride=1, shade=False)
plt.show()


# 2D
def scatter_hist(x, y, ax, ax_histx, ax_histy):
    # no labels
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    ax.spines['left'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_aspect('equal', adjustable='box')

    # the scatter plot:
    ax.scatter(x, y)

    # now determine nice limits by hand:
    binwidth = 0.25
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax/binwidth) + 1) * binwidth

    bins = np.arange(-lim, lim + binwidth, binwidth)
    ax_histx.hist(
        x, bins=bins, density=True, color="tab:cyan")

    # n, bins, patches = ax_histx.hist(
    #     x, bins=bins, density=True, color="tab:cyan")
    # ax_x2 = ax_histx.twinx()
    # print(f"len n is {len(n)}, n is {n}")  # 34
    # print(f"len bins is {len(bins)}, bins is {bins}")  # 35 每个bin左右两侧的值，不是bin中心的值

    # ax_histx.plot(bins[:-1], n*len(x))

    ax_histy.hist(y, bins=bins, density=True,
                  orientation='horizontal', color="y")


fig = plt.figure(figsize=(6, 6))
gs = fig.add_gridspec(2, 2,  width_ratios=(4, 1), height_ratios=(1, 4),
                      left=0.1, right=0.9, bottom=0.1, top=0.9,
                      wspace=0.05, hspace=0.05)
ax = fig.add_subplot(gs[1, 0])
ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)
# Draw the scatter plot and marginals.
scatter_hist(x, y, ax, ax_histx, ax_histy)
# plt.show()
