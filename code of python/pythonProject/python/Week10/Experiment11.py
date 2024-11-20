#1.了解NumPy数组的基本属性
import numpy as np
np.__version__             # 检查NumPy版本
a = np.arange(15).reshape(3, 5)
a
type(a)                    # 检查a的数据类型
a.shape                    # 检查a的形状
a.ndim                     # 检查a的维度
a.itemsize                 # 每个元素的字节大小
a.size                     # 检查a的元素数量
a.dtype                    # 检查数据类型

#2.创建NumPy数组的各种方法
b1 = np.array([1, 3, 5, 7, 9])
b1.dtype
b2 = np.array([1, 3, 5, 7, 9], dtype='float')
b2.dtype

np.arange(1, 11, 2)
np.random.randn(3, 4)
np.random.randint(1, 100, 5)
np.random.randint(1, 100, (5, 3))
np.random.uniform(1, 3, size=(3, 4))
np.array([(1, 2, 3), (4, 5, 6)])
b3 = np.arange(1, 7).reshape(2, 3)
np.zeros((3, 4))
np.ones((3, 4))
np.eye(5)
np.full((3, 4), 1.5)
np.tile(b3, 2)

np.linspace(1, 2, 10)
np.linspace(1, 2, 10, endpoint=False)
np.linspace(-2 * np.pi, 2 * np.pi, 100)

#3.索引访问Numpy数组的各种方法
a = np.arange(10, 20)
a[0], a[-1], a[2:5], a[[1, 4, 5]]
a[-3:], a[::2], a[::-1]
a > 15
a[a > 15]

b = np.arange(24).reshape(4, 6)
b[1]
b[1, 2]
b[:, 2]
b[1:, 1:3]
b[:, ::2]

c = b[1]                # c是b[1]的视图
c[0] = 100
b[1, 0]                 # 修改b的元素
d = b[2].copy()         # d是b[2]的复制
d[0] = 200
b[2, 0]                 # b的元素不会被修改

#4.数组基本运算
a = np.arange(1, 6)
a + 5, a * 2, a / 2, 10 - a
b = np.arange(10, 15)
a + b, a * b, a / b

#5.统计函数
np.random.seed(7)
a = np.random.rand(3, 4)
np.mean(a), a.mean()
np.mean(a, axis=0), a.mean(axis=0)
np.mean(a, axis=1)
np.var(a), np.std(a)
np.sin(a), np.round(a, 2)
a[1, ::2] = np.nan
np.isnan(a), np.isnan(a).sum()
np.sum(a), np.nansum(a)

#6.排序练习
np.random.seed(7)
b = np.random.randint(1, 20, size=10)
c = b.copy()
b.sort()
np.sort(c)
np.argmax(c), np.argmin(c)
np.argsort(c)
c[np.argsort(-c)]

#7.组合和拆分数组
a = np.arange(24).reshape(4, 6)
h1, h2 = np.hsplit(a, 2)
v1, v2 = np.vsplit(a, 2)
np.vstack((v1, v2))
np.hstack((h1, h2))

#9.练习
# (1) 创建一个9x9的全1数组，并将四边修改为0
ar = np.ones((9, 9))
ar[0] = 0
ar[-1] = 0
ar[:, 0] = 0
ar[:, -1] = 0
ar

# (2) 在区间[1, 6]内生成1000个随机整数，统计每个整数出现的次数
from collections import Counter
np.random.seed(7)
data = np.random.randint(1, 7, 1000)
print('Counter(data)\n', Counter(data))
print('unique(data)\n', np.unique(data))
for i in np.unique(data):
    print(i, np.sum(data == i))

# (3) 插入和删除数组元素
ar = np.arange(4)
ar = np.append(ar, 10)
ar = np.insert(ar, 2, 5)
ar = np.delete(ar, [2, 3])

# (4) 数组矩阵乘法
ar1 = np.arange(6).reshape(2, 3)
ar2 = np.arange(6).reshape(3, 2)
np.dot(ar1, ar2)

# (5) 生成符合N(70, 100)分布的50名同学成绩，并排序、求最大、最小和均值
ar = np.random.normal(loc=70, scale=10, size=50)
ar.sort()
ar.max()
ar.min()
ar.mean()
