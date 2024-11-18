#0-6,1000散点
import matplotlib.pyplot as plt
import numpy as np

# 在 x=0-6 范围内生成 1000 个随机散点
x = np.random.uniform(0, 6, 1000)  # 在 0 到 6 的区间生成均匀分布的 x 值
y = np.random.uniform(2, 9, 1000)  # 根据 y 的值范围生成随机 y 值

# 绘制散点图
plt.scatter(x, y, alpha=0.6, edgecolor='k', s=10)  # alpha 控制透明度，s 控制点的大小
plt.title("Random Scatter Points in Range")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
