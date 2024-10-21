name = ['A','B','C','D']
tel = ['1234','5678','0000','1111']

tel_index = [name.index('D')]
print(tel_index)

tel_number = tel[name.index('D')]
print(tel_number)


item = [('name','Gumby'),('age',42)]
print(type(item))
d = dict(item)
print(type(d))

d = dict(name = 'Gumby',age = '42')
print(d)

'''
a = []
a[42] = 'name'
a = {}
'''
a = {}
a['name'] = 'alice'
print(a)


