import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 学院及专业名称
colleges = ["会计", "金融", "马列", "外语", "人文", "旅游", "软件", "信息", "工商", "财税",
            "国贸", "经济", "统计", "数学", "体育", "测绘"]
majors_per_college = 2  # 每个学院有2个专业
students_per_class = random.randint(45, 50)  # 每个班级的人数

# 生成学院、专业和班级信息
students = []
student_id = 2018160101
for college in colleges:
    for major_num in range(1, majors_per_college + 1):
        for class_num in range(1, 4):  # 每个专业有3个班
            class_name = f"{college}专业{major_num}班{class_num}"
            for _ in range(students_per_class):
                student_info = {
                    "学号": student_id,
                    "学院": college,
                    "专业": f"{college}专业{major_num}",
                    "班级": class_name
                }
                students.append(student_info)
                student_id += 1

# 保存为Excel文件
df_students = pd.DataFrame(students)
df_students.to_excel("students.xlsx", index=False)

courses = ["高数一", "线性代数", "英语一", "马克思原理"]
for college in colleges:
    for major_num in range(1, majors_per_college + 1):
        for course_num in range(5, 21):
            course_name = f"{college}专业{major_num}课程{course_num - 4}"
            courses.append(course_name)

# 学生选课
df_students["选课"] = df_students.apply(lambda row: random.sample(courses, 12), axis=1)
df_students.to_excel("students_courses.xlsx", index=False)

# 课程班级
course_classes = {}
for course in courses:
    course_classes[course] = []
    num_students = df_students[df_students["选课"].apply(lambda x: course in x)].shape[0]
    num_classes = num_students // 45 + 1
    for i in range(1, num_classes + 1):
        course_classes[course].append(f"{course}班{i}")

# 生成成绩
def generate_scores():
    return np.random.normal(loc=75, scale=5, size=1)[0]

df_students["成绩"] = df_students["选课"].apply(lambda x: {course: generate_scores() for course in x})
df_students.to_excel("students_scores.xlsx", index=False)


# 获取某个班级的成绩
class_scores = df_students[df_students["班级"] == "会计专业1班1"]["成绩"].values[0].values()

# 将 dict_values 转换为普通列表
class_scores_list = list(class_scores)

# 成绩分布统计
score_bins = [0, 60, 70, 80, 90, 100]
score_labels = ['60以下', '60-70', '70-80', '80-90', '90-100']

# 统计每个区间内的学生人数
score_counts = []
for i in range(len(score_bins)-1):
    # 使用 numpy 逻辑比较符进行比较，并统计每个区间内的学生数量
    count = np.sum((np.array(class_scores_list) >= score_bins[i]) & (np.array(class_scores_list) < score_bins[i+1]))
    score_counts.append(count)

# 设置中文字体
plt.rcParams['font.family'] = ['SimHei']  # 设置为黑体
plt.rcParams['axes.unicode_minus'] = False  # 显示负号

# 绘制柱状图
plt.bar(score_labels, score_counts)
plt.xlabel("成绩区间")
plt.ylabel("人数")
plt.title("成绩分布柱状图")
plt.show()


# 简单加权计算（假设每门课权重相同）
df_students["加权成绩"] = df_students["成绩"].apply(lambda x: np.mean(list(x.values())))


# 统计不同加权成绩段的学生人数
score_bins = [0, 60, 70, 80, 90, 100]
score_labels = ['60以下', '60-70', '70-80', '80-90', '90-100']

# 统计每个区间内的学生人数
score_counts = []
for i in range(len(score_bins)-1):
    count = np.sum((df_students['加权成绩'] >= score_bins[i]) & (df_students['加权成绩'] < score_bins[i+1]))
    score_counts.append(count)

# 绘制折线图
plt.plot(score_labels, score_counts, marker='o', linestyle='-', color='b')
plt.xlabel('加权成绩区间')
plt.ylabel('学生人数')
plt.title('各加权成绩段的学生人数分布')
plt.grid(True)
plt.show()

# 不及格学生
failed_students = df_students[df_students["成绩"].apply(lambda x: any(score < 60 for score in x.values()))]
failed_students.to_excel("failed_students.xlsx", index=False)

# 加权成绩排序
df_students_sorted = df_students.sort_values(by="加权成绩", ascending=False)
df_students_sorted.to_excel("students_sorted.xlsx", index=False)


# 各专业前10名
top_10_students = []
for college in colleges:
    for major_num in range(1, majors_per_college + 1):
        major_students = df_students[(df_students["学院"] == college) &
                                      (df_students["专业"] == f"{college}专业{major_num}")]
        top_10 = major_students.nlargest(10, "加权成绩")
        top_10_students.append(top_10)

top_10_students_df = pd.concat(top_10_students)
top_10_students_df.to_excel("top_10_students.xlsx", index=False)
