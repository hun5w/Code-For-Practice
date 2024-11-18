# 1. 定义一个无参函数，打印姓名
def print_name():
    print("wjj")

print_name()

# 2. 定义一个两个参数的重复打印函数
def repeat_print(string, times):
    for _ in range(times):
        print(string)

repeat_print("0223935", 10)

# 3. 定义一个函数，分解小于10000的正整数的各位数字，并返回元组
def split_digits(number):
    if 0 < number < 10000:
        return tuple(int(digit) for digit in str(number))
    else:
        return "Number must be less than 10000"

number = 2024
digits = split_digits(number)
print(f"数字 {number} 的各位数字为：{digits}")

# 4. 计算BMI并返回结果
def getBMI(height, weight):
    BMI = weight / (height ** 2)
    if BMI < 18:
        category = "偏瘦"
    elif 18 <= BMI < 25:
        category = "正常体重"
    elif 25 <= BMI < 30:
        category = "超重"
    elif 30 <= BMI < 35:
        category = "轻度肥胖"
    elif 35 <= BMI < 40:
        category = "中度肥胖"
    else:
        category = "重度肥胖"
    return BMI, category

height = float(input("请输入身高（米）："))
weight = float(input("请输入体重（公斤）："))
bmi, category = getBMI(height, weight)
print(f"BMI值: {bmi:.2f}, 肥胖程度: {category}")
