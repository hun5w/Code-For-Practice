#嘉宾名单
List = ['laoda','pangmao','dingdongji']
print(f'请{List[0]}共进晚餐')
print(f'请{List[1]}共进晚餐')
print(f'请{List[2]}共进晚餐')

#修改嘉宾名单
print(f'\n{List[0]}无法赴约')
List[0] = 'pnx'
print(f'请{List[0]}共进晚餐')
print(f'请{List[1]}共进晚餐')
print(f'请{List[2]}共进晚餐')

#添加嘉宾
print('找到了一个更大的餐桌')
List.insert(0,'tjq')
List.insert(2,'xzy')
List.append('pnx2')
print(f'\n请{List[0]}共进晚餐')
print(f'请{List[1]}共进晚餐')
print(f'请{List[2]}共进晚餐')
print(f'请{List[3]}共进晚餐')
print(f'请{List[4]}共进晚餐')