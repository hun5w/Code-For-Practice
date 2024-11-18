#生成1000个N(1, 10)正态分布的随机小数，绘制箱线图。

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 生成符合N(1, 10)分布的随机数
x = np.random.normal(1, 10**(1/2), 1000)

# 绘制箱线图
plt.boxplot(x)
plt.title('正态分布箱线图')
plt.show()

# 打印方差
print('方差:', x.var())  # 方差应近似10
