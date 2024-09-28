#浅拷贝 copy()函数 只复制对象本身，嵌套对象仍引用原始对象
A=['I',[2,3]]
B=A.copy()
print(A)
print(B)
print(id(A[0]))
print(id(B[0]))
B.append([3,4])

B[0]='hi'

print(A)
print(B)

print(id(A[0]))
print(id(B[0]))


d = {'a':1}
print(d.get('d','none'))

#创建一个字典


