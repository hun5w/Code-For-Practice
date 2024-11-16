
def funA(x,y,z):
    print(x,y,z)

funA("hello",10,True)

import random as rm

#期末考试，五门成绩，总分排序
xin = "唐张彭魏徐严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤方"
ming1 = "家宇能百志航旻浩尊振弘诺远龙寅立伟昀林仕译恺曜晨恺聪宸辉烁诚博玄彦耀伦寅诺江海曜雷海岳迪翰宽博郎"
ming2 = "祺航西川毅启浩磊郎彦云龙伦航曜翔杉余高远悟浩唯译"


# 生成随机成绩，并调整到目标平均值的函数
def examination(n, target_averages):
    """
    生成五场考试的随机成绩，并调整每场考试的平均成绩为指定的目标平均值。
    """
    Grades = []  # 用于存放每场考试的成绩
    ranges = [(60, 95), (70, 95), (80, 95), (65, 90), (75, 95)]  # 五场考试的分数范围

    # 遍历五场考试
    for i in range(len(ranges)):
        low, high = ranges[i]
        raw_grades = [rm.randint(low, high) for _ in range(n)]  # 随机生成n个学生的成绩
        adjusted_grades = adjust_average(raw_grades, target_averages[i])  # 调整每场考试的平均成绩
        Grades.append(adjusted_grades)

    return Grades  # 返回所有考试的成绩


# 调整平均值的函数
def adjust_average(grades, target_average):
    current_average = sum(grades) / len(grades)
    adjustment = target_average - current_average
    adjusted_grades = [int(grade + adjustment) for grade in grades]
    return adjusted_grades


# 生成学生信息
def CreateStudent(n, Grades):
    Students = []
    for i in range(n):
        name = (xin[rm.randint(0, len(xin) - 1)] +
                ming1[rm.randint(0, len(ming1) - 1)] +
                ming2[rm.randint(0, len(ming2) - 1)])
        number = rm.randint(1, 60)
        student = [name, f'2022{number:02}']

        # 将五门成绩添加到学生信息中
        student.extend(Grades[j][i] for j in range(5))  # 五门成绩
        total_score = sum(Grades[j][i] for j in range(5))  # 计算总成绩
        student.append(total_score)  # 添加总成绩
        Students.append(student)
    return Students


if __name__ == "__main__":
    n = 55
    target_averages = [75, 85, 90, 80, 88]  # 设定五门考试的目标平均值

    # 生成随机成绩并调整到目标平均值
    Grades = examination(n, target_averages)

    # 生成学生
    Students = CreateStudent(n, Grades)

    # 按总分排序，使用lambda表达式
    Students_sorted = sorted(Students, key=lambda student: student[-1], reverse=True)  # 按总分降序排序

    # 打印排序后的学生信息
    print("按总成绩排序后的学生信息:")
    for student in Students_sorted:
        print(student)
