import numpy as np
import matplotlib.pyplot as plt

# 定义函数及其导数
x = np.linspace(-10, 10, 500)  # 定义x在[-10, 10]区间上的取值
y = x**3 - 6*x**2 + 4*x + 2  # 多项式函数
dy = 3*x**2 - 12*x + 4       # 一阶导数
ddy = 6*x - 12               # 二阶导数

# 创建图形和子图
fig = plt.figure(figsize=(10, 8))

# 绘制多项式图
ax1 = fig.add_subplot(311)
ax1.plot(x, y, 'r-', label="y = x^3 - 6x^2 + 4x + 2")  # 红色实线
ax1.set_title("Polynomial")
ax1.legend()

# 绘制一阶导数图
ax2 = fig.add_subplot(312)
ax2.plot(x, dy, 'b--', label="y' = 3x^2 - 12x + 4")  # 蓝色虚线
ax2.set_title("First Derivative")
ax2.legend()

# 绘制二阶导数图
ax3 = fig.add_subplot(313)
ax3.plot(x, ddy, 'go', label="y'' = 6x - 12")  # 绿色实心圆点
ax3.set_title("Second Derivative")
ax3.legend()

# 调整布局并显示图形
plt.tight_layout()
plt.show()
