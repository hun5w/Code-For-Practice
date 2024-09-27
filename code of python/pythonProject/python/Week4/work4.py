

'课堂练习，随机生成1w个1-10的数，用set去重'

import random as rm



# 生成 1w 个随机数
rm_numbers = [rm.randint(1, 10) for _ in range(10000)]

# 使用 set 去重
unique_numbers = set(rm_numbers)

# 输出去重后的结果
print(unique_numbers)
print(f"去重后的数量: {len(unique_numbers)}")

'''
创建一个字典：info
1.以'张三'，'李四'为key
“张三”的value包含(年龄: 20,性别:男，爱好:打球)“李四”的value包含 (年龄: 25,性别:男，爱好:学习)打印info。
2、再添加一条信息key为小红，value为: 年龄18,性别女，爱好旅游。
3、更改李四的年龄为40。.
4、删除张三的信息。
'''

