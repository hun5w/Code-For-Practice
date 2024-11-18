import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 100)
fig = plt.figure()  # 创建一个Figure对象

# 第一个子图
ax1 = fig.add_subplot(221)
ax1.plot(x, x)
ax1.set_title("y = x")

# 第二个子图
ax2 = fig.add_subplot(222)
ax2.plot(x, -x)
ax2.set_title("y = -x")

# 第三个子图
ax3 = fig.add_subplot(223)
ax3.plot(x, x**2)
ax3.set_title("y = x^2")

# 第四个子图
ax4 = fig.add_subplot(224)
ax4.plot(x, np.log(x))
ax4.set_title("y = log(x)")

plt.tight_layout()
plt.show()
