'课堂练习，随机生成1w个1-10的数，用set去重'

import random as rm

# 生成 1w 个随机数
rm_numbers = [rm.randint(1, 10) for _ in range(10000)]

# 使用 set 去重
unique_numbers = set(rm_numbers)

# 输出去重后的结果
print(unique_numbers)
print(f"去重后的数量: {len(unique_numbers)}")



import random as rm

xin = "唐张彭魏徐严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤方"
ming1 = "家宇能百志航旻浩尊振弘诺远龙寅立伟昀林仕译恺曜晨恺聪宸辉烁诚博玄彦耀伦寅诺江海曜雷海岳迪翰宽博郎"
ming2 = "祺航西川毅启浩磊郎彦云龙伦航曜翔杉余高远悟浩唯译"

# 生成随机成绩
def examination(n):
    Grades = []
    ranges = [(20, 26), (30, 36), (40, 46)]
    for low, high in ranges:
        Grade = [rm.randint(low, high) for _ in range(n)]
        Grades.append(Grade)
    return Grades

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
def calculate_total_scores_p(students):
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
    n = 60
    target = 12
    Grades = examination(n)

    # 计算每场考试的平均值和方差
    for i, grade in enumerate(Grades):
        avg = calculate_average(grade)
        var = calculate_p(grade)
        print(f"第 {i + 1} 场考试的平均值: {avg:.2f}")
        print(f"第 {i + 1} 场考试的方差: {var:.2f}")

    # 生成学生
    Students = CreateStudent(n, Grades)

    # 打印学生信息
    for student in Students:
        print(student)

    # 计算总成绩方差
    total_scores_variance = calculate_total_scores_p(Students)
    print(f"所有学生总成绩的方差: {total_scores_variance:.2f}")

    # 统计某门课程各个分数段的人数
    course_index = 0  # 选择第一门课程
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # 分数段范围
    distribution = count_score_distribution(Grades[course_index], bins)
    print(f"第 {course_index + 1} 门课程各个分数段的人数:")
    for lower, upper, count in distribution:
        print(f"{lower}-{upper}: {count}人")
