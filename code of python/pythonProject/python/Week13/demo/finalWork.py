import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 1. 随机生成各个学院各个专业各个班级的学生，数据保存到excel文件中

# 定义学院、专业
colleges = ["会计", "金融", "马列", "外语", "人文", "旅游", "软件", "信息", "工商", "财税",
            "国贸", "经济", "统计", "数学", "体育", "测绘"]
majors = {
    "会计": ["会计专业1", "会计专业2"],
    "金融": ["金融专业1", "金融专业2"],
    "马列": ["马列专业1", "马列专业2"],
    "外语": ["外语专业1", "外语专业2"],
    "人文": ["人文学科1", "人文学科2"],
    "旅游": ["旅游专业1", "旅游专业2"],
    "软件": ["软件专业1", "软件专业2"],
    "信息": ["信息专业1", "信息专业2"],
    "工商": ["工商管理1", "工商管理2"],
    "财税": ["财税专业1", "财税专业2"],
    "国贸": ["国贸专业1", "国贸专业2"],
    "经济": ["经济专业1", "经济专业2"],
    "统计": ["统计专业1", "统计专业2"],
    "数学": ["数学专业1", "数学专业2"],
    "体育": ["体育专业1", "体育专业2"],
    "测绘": ["测绘专业1", "测绘专业2"]
}

# 生成学生学号函数
def generate_student_id(college, major, class_num, student_counter):
    return f"{college[:2]}{major[:2]}{class_num:02d}{str(student_counter).zfill(2)}"

# 每个班级50个学生
students_per_class = 50

# 每个学院分配的班级数
college_classes = {
    "会计": 6, "金融": 6, "马列": 6, "外语": 6, "人文": 6, "旅游": 6,
    "软件": 8, "信息": 8, "工商": 6, "财税": 6, "国贸": 6, "经济": 6,
    "统计": 6, "数学": 6, "体育": 6, "测绘": 6
}

students = []
for college in colleges:
    num_classes_in_college = college_classes[college]
    for major in majors[college]:
        for class_num in range(1, num_classes_in_college + 1):  # 确保班级编号正确
            student_counter = 1
            for _ in range(students_per_class):
                student_id = generate_student_id(college, major, class_num, student_counter)
                students.append({
                    "学院": college,
                    "专业": major,
                    "班级": f"{major}班级{class_num}",
                    "学号": student_id
                })
                student_counter += 1

df_students = pd.DataFrame(students)
df_students.to_excel("students_data.xlsx", index=False)
print("学生数据已成功生成并保存到Excel文件")

# 2. 随机生成课程数据
fixed_courses = ["高数一", "线性代数", "英语一", "马克思原理"]

def generate_courses(college, major):
    courses = fixed_courses.copy()
    for i in range(1, 17):
        course_name = f"{college}{major}课程{i}"
        courses.append(course_name)
    random.shuffle(courses)
    return courses[:20]  # 确保每个专业有20门课程

courses_data = []
for college in colleges:
    for major in majors[college]:
        courses = generate_courses(college, major)
        for course in courses:
            courses_data.append({
                "学院": college,
                "专业": major,
                "课程": course
            })

df_courses = pd.DataFrame(courses_data)
df_courses.to_excel("courses_data.xlsx", index=False)
print("课程数据已成功生成并保存到Excel文件")

# 3. 随机生成学生的选课数据
min_courses_per_semester = 4
max_courses_per_semester = 6
min_total_courses = 9
max_total_courses = 12

students = []
student_counter = 1
num_students_in_major = 50

for college in colleges:
    for major in majors[college]:
        courses = generate_courses(college, major)
        for student_num in range(num_students_in_major):
            student_id = generate_student_id(college, major, 1, student_counter)
            student_counter += 1
            total_courses = random.randint(min_total_courses, max_total_courses)
            semester_1_courses = random.sample(courses, random.randint(min_courses_per_semester, max_courses_per_semester))
            remaining_courses = list(set(courses) - set(semester_1_courses))
            semester_2_courses = random.sample(remaining_courses, total_courses - len(semester_1_courses))

            students.append({
                "学号": student_id,
                "学院": college,
                "专业": major,
                "学期1课程": ", ".join(semester_1_courses),
                "学期2课程": ", ".join(semester_2_courses)
            })

df_students = pd.DataFrame(students)
df_students.to_excel("student_courses.xlsx", index=False)
print("学生选课数据已成功生成并保存到Excel文件")

# 4. 根据选课情况生成课程班级
def generate_class_for_courses(student_courses_df, courses_data_df):
    course_class_mapping = []
    course_class_count = {}

    # 统计每门课程的选课人数
    for _, row in student_courses_df.iterrows():
        semester_1_courses = row["学期1课程"].split(", ")
        semester_2_courses = row["学期2课程"].split(", ")
        all_courses = semester_1_courses + semester_2_courses

        for course in all_courses:
            if course not in course_class_count:
                course_class_count[course] = 0
            course_class_count[course] += 1

    # 为每门课程生成班级
    for course, num_students in course_class_count.items():
        num_classes = (num_students // 50) + (1 if num_students % 50 > 0 else 0)

        for class_num in range(1, num_classes + 1):
            course_class_mapping.append({
                "课程": course,
                "班级": f"{course}_班级{class_num}"
            })

    df_course_classes = pd.DataFrame(course_class_mapping)
    df_course_classes.to_excel("course_classes.xlsx", index=False)
    print("课程班级数据已成功生成并保存到Excel文件")

# 加载学生选课数据和课程数据
df_students = pd.read_excel("student_courses.xlsx")
df_courses = pd.read_excel("courses_data.xlsx")

# 生成课程班级
generate_class_for_courses(df_students, df_courses)

# 5. 生成成绩数据
def generate_scores_for_class(course, class_name, student_ids):
    if len(student_ids) == 0:
        print(f"警告：班级 {class_name} 中没有找到学生，课程：{course}")
        return []  # 如果没有学生，直接返回空列表

    student_scores = []
    low_scores_count = random.randint(1, 2)
    high_scores_count = random.randint(7, 10)
    medium_scores_count = len(student_ids) - low_scores_count - high_scores_count

    low_scores = np.random.randint(50, 60, low_scores_count)
    high_scores = np.random.randint(90, 101, high_scores_count)
    medium_scores = np.random.normal(75, 2, medium_scores_count)
    medium_scores = np.clip(medium_scores, 70, 80)

    all_scores = np.concatenate([low_scores, high_scores, medium_scores])
    np.random.shuffle(all_scores)

    # 生成成绩并与学生学号对应
    for idx, score in zip(range(len(student_ids)), all_scores):
        student_ID = student_ids[idx]
        student_scores.append({
            "学号": student_ID,
            "课程": course,
            "班级": class_name,  # 确保班级列被正确添加
            "成绩": round(score, 2)
        })

    return student_scores

# 加载学生和课程班级数据
df_students = pd.read_excel("students_data.xlsx")
df_course_classes = pd.read_excel("course_classes.xlsx")

# 用于存储所有学生成绩的列表
all_student_scores = []

# 遍历每个课程班级
for _, row in df_course_classes.iterrows():
    course = row["课程"]
    class_name = row["班级"]

    # 获取当前班级所有学生的学号
    class_students = df_students[df_students["班级"] == class_name]["学号"].values

    # 调试：输出班级和学生学号，确保数据正确
    if len(class_students) > 0:
        print(f"班级 {class_name} 共有 {len(class_students)} 名学生")
    else:
        print(f"警告：班级 {class_name} 没有学生")

    # 生成该班级的学生成绩
    student_scores = generate_scores_for_class(course, class_name, class_students)
    all_student_scores.extend(student_scores)

# 将所有学生成绩保存到Excel文件
df_scores = pd.DataFrame(all_student_scores)

# 如果成绩数据为空，输出警告
if df_scores.empty:
    print("警告：没有生成学生成绩数据！")
else:
    df_scores.to_excel("student_scores.xlsx", index=False)
    print("学生成绩数据已成功生成并保存到Excel文件")

# 6. 统计课程班级的成绩分布，并且生成柱状图（Matplotlib）。60分以下，60-70，70-80，80-90，90-100。

# 载入学生成绩数据
df_scores = pd.read_excel("student_scores.xlsx")

# 统计成绩分布
def score_distribution_for_class(class_name):
    # 获取指定班级的成绩数据
    class_scores = df_scores[df_scores["班级"] == class_name]["成绩"]

    # 定义分数区间
    bins = [0, 60, 70, 80, 90, 100]
    labels = ['60以下', '60-70', '70-80', '80-90', '90-100']

    # 使用 pd.cut 计算成绩分布
    score_bins = pd.cut(class_scores, bins=bins, labels=labels, right=False)

    # 统计每个区间的人数
    score_counts = score_bins.value_counts().sort_index()

    return score_counts

# 选择一个班级进行统计和绘图
class_name = "高数一_班级1"  # 假设我们选择了一个班级
score_counts = score_distribution_for_class(class_name)

# 设置中文字体
plt.rcParams['font.family'] = ['SimHei']  # 设置为黑体
plt.rcParams['axes.unicode_minus'] = False  # 显示负号

# 绘制柱状图
plt.figure(figsize=(8, 6))
score_counts.plot(kind='bar', color='skyblue')

# 设置图表标题和标签
plt.title(f"{class_name} 成绩分布", fontsize=14)
plt.xlabel('成绩区间', fontsize=12)
plt.ylabel('学生人数', fontsize=12)

# 显示柱状图
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 6. 统计课程班级的成绩分布，并且生成柱状图（Matplotlib）。60分以下，60-70，70-80，80-90，90-100。

# 载入学生成绩数据
df_scores = pd.read_excel("student_scores.xlsx")

# 统计成绩分布
def score_distribution_for_class(class_name):
    # 获取指定班级的成绩数据
    class_scores = df_scores[df_scores["班级"] == class_name]["成绩"]

    # 定义分数区间
    bins = [0, 60, 70, 80, 90, 100]
    labels = ['60以下', '60-70', '70-80', '80-90', '90-100']

    # 使用 pd.cut 计算成绩分布
    score_bins = pd.cut(class_scores, bins=bins, labels=labels, right=False)

    # 统计每个区间的人数
    score_counts = score_bins.value_counts().sort_index()

    return score_counts

# 选择一个班级进行统计和绘图
class_name = "高数一_班级1"  # 假设我们选择了一个班级
score_counts = score_distribution_for_class(class_name)

# 设置中文字体
plt.rcParams['font.family'] = ['SimHei']  # 设置为黑体
plt.rcParams['axes.unicode_minus'] = False  # 显示负号

# 绘制柱状图
plt.figure(figsize=(8, 6))
score_counts.plot(kind='bar', color='skyblue')

# 设置图表标题和标签
plt.title(f"{class_name} 成绩分布", fontsize=14)
plt.xlabel('成绩区间', fontsize=12)
plt.ylabel('学生人数', fontsize=12)

# 显示柱状图
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# 7. 对大一同学成绩进行加权计算，统计各个学生加权成绩，用折线图表示各个加权段之间的人数（文件处理、Matplotlib、加权你们根据学院来定，也可以是权重一样）。

# 随机生成的成绩数据
students_data = pd.read_excel("student_courses.xlsx")  # 假设学生成绩已经存在
# 示例: 生成每个学生的加权成绩数据

# 随机生成加权成绩的示例 (成绩范围是60-100)
def generate_weighted_score():
    # 假设每个学生有9到12门课程，每门课程成绩60到100分
    return [random.randint(60, 100) for _ in range(random.randint(9, 12))]

# 给每个学生生成加权成绩
students_data["加权成绩"] = students_data.apply(lambda row: sum(generate_weighted_score()) / len(generate_weighted_score()), axis=1)

# 统计加权成绩段的人数
def categorize_weighted_score(score):
    if score < 60:
        return "60以下"
    elif score < 70:
        return "60-70"
    elif score < 80:
        return "70-80"
    elif score < 90:
        return "80-90"
    else:
        return "90-100"

# 分类加权成绩
students_data["成绩段"] = students_data["加权成绩"].apply(categorize_weighted_score)

# 统计每个成绩段的学生人数
score_distribution = students_data["成绩段"].value_counts().sort_index()

# 绘制折线图
plt.figure(figsize=(8, 6))
score_distribution.plot(kind='line', marker='o', color='b')

# 设置图表标题和标签
plt.title("大一同学加权成绩分布", fontsize=14)
plt.xlabel("成绩段", fontsize=12)
plt.ylabel("学生人数", fontsize=12)

# 显示图表
plt.tight_layout()
plt.show()

# 保存结果到Excel
students_data.to_excel("students_with_weighted_scores.xlsx", index=False)

# 8. 统计各个班存在课程不及格的学生人数，并且将不及格的学生：学院、专业、班级、姓名、学号、课程、成绩保存到Excel表中.

# 读取成绩数据，假设每个班级都存储在不同的Excel文件中
def load_class_data(class_name):
    try:
        return pd.read_excel(f"{class_name}.xlsx")  # 每个班的Excel文件
    except FileNotFoundError:
        print(f"文件 {class_name}.xlsx 未找到")
        return pd.DataFrame()

# 我们有一个包含学院、专业、班级、学生姓名等信息的文件
students_info = pd.read_excel("students_data.xlsx")  # 学生基本信息，包含学院、专业、班级等

# 用于保存不及格学生的列表
failed_students = []

# 设定不及格的分数线
passing_score = 60

# 假设班级列表
class_names = students_info["班级"].unique()  # 根据学生信息中的班级获取所有班级的名称

# 遍历每个班级，找到不及格学生
for class_name in class_names:
    # 加载班级成绩数据
    class_data = load_class_data(class_name)

    # 如果班级数据存在
    if not class_data.empty:
        # 找到不及格的学生
        failed_students_in_class = class_data[class_data["成绩"] < passing_score]

        # 获取对应学生的基本信息，并保存到 failed_students 列表中
        for _, row in failed_students_in_class.iterrows():
            student_info = students_info[students_info["班级"] == class_name]
            if not student_info.empty:
                # 获取对应学生的信息
                student_info_row = student_info.iloc[0]  # 假设每个班级只有一名专业
                failed_students.append({
                    "学院": student_info_row["学院"],
                    "专业": student_info_row["专业"],
                    "班级": class_name,
                    "姓名": student_info_row["姓名"],  # 假设有姓名字段
                    "学号": student_info_row["学号"],
                    "课程": row["课程"],
                    "成绩": row["成绩"]
                })

# 将不及格的学生信息保存到 Excel 文件
failed_students_df = pd.DataFrame(failed_students)
failed_students_df.to_excel("failed_students.xlsx", index=False)

print("不及格学生信息已成功保存到 failed_students.xlsx")