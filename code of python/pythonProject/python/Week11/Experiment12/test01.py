#利用[2, 3, 5, 10, 8]列表数据绘制折线图、柱形图、饼图。
import matplotlib.pyplot as plt

# 设置字体和负号显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据
x = [2, 3, 5, 10, 8]
labels = list('abcde')

# 折线图
plt.plot(x, 'b-')
plt.title('折线图')
plt.show()

# 柱形图
plt.figure()
plt.bar(labels, x)
plt.title('柱形图')
plt.show()

# 饼图
plt.figure()
explode = [0, 0, 0.1, 0.2, 0]
plt.pie(x, explode=explode, labels=labels, autopct='%1.1f%%')
plt.title('饼图')
plt.show()
