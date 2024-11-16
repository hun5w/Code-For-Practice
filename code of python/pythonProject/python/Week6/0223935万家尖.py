import random as rm

xin = "唐张彭魏徐严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤方"
ming1 = "家宇能百志航旻浩尊振弘诺远龙寅立伟昀林仕译恺曜晨恺聪宸辉烁诚博玄彦耀伦寅诺江海曜雷海岳迪翰宽博郎"
ming2 = "祺航西川毅启浩磊郎彦云龙伦航曜翔杉余高远悟浩唯译"


# 生成随机成绩，并调整到目标平均值的函数
def examination(n, target_averages):
    """
    生成三场考试的随机成绩，并调整每场考试的平均成绩为指定的目标平均值。

    :param n: 学生人数
    :param target_averages: 目标的平均成绩列表
    :return: 返回一个包含三场考试成绩的列表
    """
    # 创建一个空列表用于存放每场考试的成绩
    Grades = []

    # 定义每场考试的分数范围
    ranges = [(60, 95), (70, 95), (80, 95)]

    # 遍历每场考试
    for i in range(len(ranges)):
        low = ranges[i][0]  # 当前考试的最低分数
        high = ranges[i][1]  # 当前考试的最高分数

        # 随机生成n个学生的成绩，分数范围在low到high之间
        raw_grades = []  # 用于存放随机生成的原始成绩
        for _ in range(n):
            grade = rm.randint(low, high)  # 生成一个随机成绩
            raw_grades.append(grade)  # 将生成的成绩添加到原始成绩列表中

        # 调整这场考试的平均值为目标平均值
        adjusted_grades = adjust_average(raw_grades, target_averages[i])

        # 将调整好的成绩加入到Grades列表中
        Grades.append(adjusted_grades)

    return Grades  # 返回所有考试的成绩

# 调整平均值的函数
def adjust_average(grades, target_average):
    current_average = calculate_average(grades)
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
        d = sum(Grades[j][i] for j in range(3))
        student.extend(Grades[j][i] for j in range(3))
        student.append(d)  # 添加总成绩
        Students.append(student)
    return Students


# 计算平均值
def calculate_average(grades):
    return sum(grades) / len(grades)


# 计算方差
def calculate_p(grades):
    mean = calculate_average(grades)
    return sum((x - mean) ** 2 for x in grades) / len(grades)

# 计算总成绩的方差
def calculate_total_p(students):
    total_scores = [student[-1] for student in students]
    return calculate_p(total_scores)

# 统计分数段分布
def count_score_distribution(grades, bins):
    distribution = [0] * (len(bins) - 1)
    for grade in grades:
        for i in range(len(bins) - 1):
            if bins[i] <= grade < bins[i + 1]:
                distribution[i] += 1
                break
    return list(zip(bins[:-1], bins[1:], distribution))


if __name__ == "__main__":
    n = 55
    target_averages = [75, 85, 90]  # 设定每门考试的目标平均值

    # 生成随机成绩并调整到目标平均值
    Grades = examination(n, target_averages)

    # 计算每场考试的平均值
    for i, grade in enumerate(Grades):
        avg = calculate_average(grade)
        print(f"第 {i + 1} 场考试的平均值: {avg:.2f}")

    # 生成学生
    Students = CreateStudent(n, Grades)

    #打印总成绩方差
    print(f"总成绩方差：{calculate_total_p(Students):.2f}")


    # 打印学生信息
    for student in Students:
        print(student)


    # 统计某门课程各个分数段的人数
    course_index = 0  # 选择第一门课程
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # 分数段范围
    distribution = count_score_distribution(Grades[course_index], bins)
    print(f"第 {course_index + 1} 门课程各个分数段的人数:")
    for lower, upper, count in distribution:
        print(f"{lower}-{upper}: {count}人")
