#矩阵的加减乘运算，链表推导式初始化矩阵

# 使用链表推导式初始化矩阵
rows, cols = 3, 3  # 矩阵的行数和列数
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
print("初始化矩阵:")
for row in matrix:
    print(row)

# 矩阵加法
def matrix_add(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
    return result

# 示例
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

sum_matrix = matrix_add(matrix1, matrix2)
print("\n矩阵加法结果:")
for row in sum_matrix:
    print(row)


# 矩阵减法
def matrix_subtract(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[matrix1[i][j] - matrix2[i][j] for j in range(cols)] for i in range(rows)]
    return result

# 示例
diff_matrix = matrix_subtract(matrix1, matrix2)
print("\n矩阵减法结果:")
for row in diff_matrix:
    print(row)


# 矩阵乘法
def matrix_multiply(matrix1, matrix2):
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("矩阵的列数必须等于另一个矩阵的行数")

    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1)) for j in range(cols2)] for i in range(rows1)]
    return result


# 示例
matrix3 = [[1, 2], [3, 4], [5, 6]]
matrix4 = [[7, 8], [9, 10]]

prod_matrix = matrix_multiply(matrix3, matrix4)
print("\n矩阵乘法结果:")
for row in prod_matrix:
    print(row)


#猜拳游戏
import random


def get_computer_choice():
    """计算机随机选择石头、剪刀、布"""
    choices = ['石头', '剪刀', '布']
    return random.choice(choices)


def get_user_choice():
    """获取用户输入的选择"""
    while True:
        user_choice = input("请输入你的选择（石头、剪刀、布）：")
        if user_choice in ['石头', '剪刀', '布']:
            return user_choice
        else:
            print("无效选择，请重新输入！")


def determine_winner(user_choice, computer_choice):
    """确定游戏结果"""
    if user_choice == computer_choice:
        return "平局"
    elif (user_choice == '石头' and computer_choice == '剪刀') or \
            (user_choice == '剪刀' and computer_choice == '布') or \
            (user_choice == '布' and computer_choice == '石头'):
        return "你赢了！"
    else:
        return "你输了！"


def play_game():
    """游戏主函数"""
    print("欢迎来到猜拳游戏！")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"你选择了: {user_choice}")
        print(f"计算机选择了: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        # 询问用户是否再来一局
        play_again = input("再来一局吗？(y/n): ")
        if play_again.lower() != 'y':
            print("感谢参与！游戏结束。")
            break


# 开始游戏
play_game()


#三角形
def can_form_triangle(a, b, c):
    """判断三条边是否能形成三角形"""
    return a + b > c and a + c > b and b + c > a


def get_input():
    """获取用户输入的三条边"""
    while True:
        try:
            a = float(input("请输入第一条边长: "))
            b = float(input("请输入第二条边长: "))
            c = float(input("请输入第三条边长: "))
            if a <= 0 or b <= 0 or c <= 0:
                print("边长必须是正数，请重新输入。")
                continue
            return a, b, c
        except ValueError:
            print("无效输入，请输入数字。")


def main():
    """程序主函数"""
    print("判断三角形是否成立")
    while True:
        a, b, c = get_input()
        if can_form_triangle(a, b, c):
            print("这三条边可以形成一个三角形。")
        else:
            print("这三条边不能形成一个三角形。")

        play_again = input("是否继续判断另一个三角形？(y/n): ")
        if play_again.lower() != 'y':
            print("感谢使用，程序结束！")
            break


# 启动程序
main()


#杨辉三角
def yanghui_triangle(n):
    triangle = []

    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]

            row.extend([last_row[j]+last_row[j + 1] for j in range(len(last_row) - 1)])
            row.append(1)
        triangle.append(row)

    for row in triangle:
        print(" " * (n))