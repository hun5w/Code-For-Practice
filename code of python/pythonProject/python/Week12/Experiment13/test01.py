# 导入必要的模块
import pandas as pd
import numpy as np  # 需要用到NumPy数组生成
from pandas import DataFrame, Series

# 显示Pandas版本
print("Pandas版本:", pd.__version__)

# 创建一个Series，索引为字符列表'a'到'f'
s = Series(np.arange(6), index=list('abcdef'))
print("\nSeries对象 s:")
print(s)

# 显示索引
print("\nSeries索引:")
print(s.index)

# 显示数据
print("\nSeries数据:")
print(s.values)

# 索引访问
print("\n按索引访问: ")
print("s['a']:", s['a'])
print("s[0]:", s.iloc[0]) # 使用 iloc 按位置索引 原代码:print("s[0]:",s[0])
print("s['a':'c']:\n", s['a':'c'])  # 包括起止位置
print("s[0:2]:\n", s[0:2])  # 左闭右开

# 修改部分数据
s['c':'e'] = 3
print("\n修改后的 Series:")
print(s)

# 统计函数
print("\n统计数据:")
print("Sum:", s.sum())
print("Mean:", s.mean())
print("Median:", s.median())

# 统计数据的频次
print("\n数据频次统计:")
print(s.value_counts())

# 返回不重复的数据列
print("\n不重复的数据:")
print(s.unique())

# 显示头3个数据
print("\n头3个数据:")
print(s.head(3))

# 显示末尾2个数据
print("\n末尾2个数据:")
print(s.tail(2))

# 创建另一个 Series
s2 = Series(np.arange(12, 30, 3), index=list('abcabc'))
print("\nSeries对象 s2:")
print(s2)

# 按索引对齐运算
print("\n按索引对齐加法 s + s2:")
print(s + s2)

# 按索引对齐乘法
print("\n按索引对齐乘法 s * s2:")
print(s * s2)
