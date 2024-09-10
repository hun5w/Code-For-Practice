import math
from math import pi


'''
1.区分整除和取余
'''
x = 7
y = 3

#取余
print(x%y)

#向上取整
print(math.ceil(x/y))

#向下取整
print(math.floor(x/y))


'''
2.在python中,不同数据类型之间的运算会遵循一定的优先级，以下是常见的数据类型优先级表，从高到低依次是：
    1.复数(complex)
    2.浮点数(float)
    3.整数(int)
    4.字符串(str)
    5.列表(list)
    6.元组(tuple)
    7.字典(dict)
    8.集合(set)
    9.布尔值(bool)
'''

'''
3.解释浮点数下0.1*3-0.3为何不等于0
'''

a = 0.1
b = 0.3
result = a * 3 - b

print(f"0.1 * 3 的结果是: {a * 3}")
print(f"0.1 * 3 - 0.3 的结果是: {result}")
print(f"结果是否等于0: {result == 0}")

#浮点数在计算机中是以二进制小数的形式存储的，
#而二进制小数无法精确表示0.1和0.3这两个十进制小数。
#只能近似表示,所以在计算机中0.1 * 3 - 0.3的结果不等于0。

'''
4.输出pi is roughly 3.14
'''
print(f"pi is roughly {pi:.10f}")
