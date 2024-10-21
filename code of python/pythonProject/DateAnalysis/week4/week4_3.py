# popitem(),[用于从字典中删除并返回一个任意的键值对 py2.x],[取最后一个键值对 py3.x]
# pop(),用于从字典中获取并删除指定键的键值对


# print
name = 'Gumby'
salutation = 'Mr'
greeting=  'Hello'
print(greeting+",",salutation,name)
#print(greeting,salutation,name,sep=',',end='!') 分隔符

'''
import xxx
from xxx import aaa
from xxx import aaa bbb ccc

from module1 import open as open1
from module2 import open as open2
防止命名冲突
'''

scoundrel = {'name':'Robin', 'boyfriend': 'opnep'}
key, value = scoundrel.popitem()
print(key)
print(value)

#交换
a,b = 1,2
print(a,b)
b,a = a,b
print(a,b)

#容器
a,b,*rest = [1,2,3,4]
print(*rest)

a,b,*c,d = [1,2,3,4]
print(a,b,c,d)

#链式赋值
'''
x = y = somefunciton()          

y = somefunction()          
x = y
'''

'''
y = somefunciton()
x = soemfunction()
'''

#使用时间函数验证
import time
def current_time():
    return time.strftime("%H:%M:%S")+f".{int(time.time()*1000)%1000:03d}"

x = y =current_time()
print(f"x:{x},y:{y}")

x = current_time()
time.sleep(1)
y = current_time()
print(f"x:{x},y:{y}")

#and or 非

name = input("please enter your name:\n")
if  name:
    print(f"your name is {name}")
else:
    print('your name is <unknow>')