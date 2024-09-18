'''
第二周周六课堂练习
'''
from math import prod
from operator import itemgetter

x=[10,20,30,40,50]
x.append(60)
x.reverse()
print(x)
x.insert(1,25)
x.pop(0)
count =x.count(30)
x.sort()
print(count)
print(x)

a=[2,30,57,28]
prod(a)

b=[(5,3),(1,2),(3,-2)]
b.sort()
print(b)
