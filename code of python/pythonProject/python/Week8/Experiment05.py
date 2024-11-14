'''
使用random库实现以下随机数的生成：
（1）随机生成一个[1,6]间的整数
（2）随机生成一个[60,100)之间的浮点数
（3）随机生成一个0到100间的奇数
（4）随机从学号列表['0200001','0200002','0200003','0200004']中抽取2名学生中奖
（5）随机打乱学号列表['0200001','0200002','0200003','0200004']，以排队回答问题
'''

import random

# (1) 随机生成一个 [1,6] 间的整数
random_integer = random.randint(1, 6)
print("随机生成的整数 [1,6]：", random_integer)

# (2) 随机生成一个 [60,100) 之间的浮点数
random_float = random.uniform(60, 100)
print("随机生成的浮点数 [60,100)：", random_float)

# (3) 随机生成一个 0 到 100 间的奇数
random_odd = random.choice(range(1, 101, 2))
print("随机生成的奇数 [0,100]：", random_odd)

# (4) 随机从学号列表中抽取 2 名学生中奖
student_ids = ['0200001', '0200002', '0200003', '0200004']
selected_students = random.sample(student_ids, 2)
print("抽中的学生学号：", selected_students)

# (5) 随机打乱学号列表，以排队回答问题
random.shuffle(student_ids)
print("打乱后的学号列表：", student_ids)


'''
2. 编写程序，计算S=1+1/3-1/5+1/7-1/9……的结果。
'''

# 设置最大项数和精度阈值
n_terms = 1000  # 最大项数上限
threshold = 1e-6  # 精度阈值

# 初始化结果和迭代项
S = 0
sign = 1  # 控制符号的变量，1表示加，-1表示减

for i in range(n_terms):
    # 计算分母
    denominator = 2 * i + 1
    # 计算当前项
    term = sign * (1 / denominator)

    # 如果当前项的绝对值小于阈值，认为收敛，可以提前终止
    if abs(term) < threshold:
        break

    # 将当前项累加到 S
    S += term

    # 切换符号
    sign = -sign

    # 跳过一些不必要的打印操作
    if i % 100 != 0:
        continue  # 跳过剩余循环体，直接进入下一次循环
    print(f"到第 {i + 1} 项时，S 的值为：{S}")

print("计算的 S 值：", S)

'''
3. 编写程序，输出公元[2000, 3000]年之间所有的闰年。
'''

for year in range(2000,3001):
    if(year % 4 == 0 and year % 400 != 0):
        print(year)

'''
4.在[1, 100]之间产生三个随机整数a，b，c，求a，b，c的最大公约数和最小公倍数。
'''
import random
import math

# 生成三个随机整数 a, b, c 在 [1, 100] 范围内
a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)

# 计算最大公约数 (GCD)
gcd_ab = math.gcd(a, b)
gcd_abc = math.gcd(gcd_ab, c)

# 计算最小公倍数 (LCM)
lcm_ab = abs(a * b) // gcd_ab
lcm_abc = abs(lcm_ab * c) // math.gcd(lcm_ab, c)

print(f"随机整数 a: {a}, b: {b}, c: {c}")
print(f"最大公约数 (GCD): {gcd_abc}")
print(f"最小公倍数 (LCM): {lcm_abc}")
