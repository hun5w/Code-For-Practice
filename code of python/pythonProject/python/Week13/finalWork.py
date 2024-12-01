import random
import pandas as pd

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

# 学生学号生成函数
def generate_student_id(base_id, number):
    return f"{base_id}{str(number).zfill(2)}"

# 每个班级50个学生
students_per_class = 50

# 总班级数为100
total_classes = 100

# 每个学院分配6个班级，软件和信息增加2个班级
college_classes = {
    "会计": 6, "金融": 6, "马列": 6, "外语": 6, "人文": 6, "旅游": 6,
    "软件": 8, "信息": 8, "工商": 6, "财税": 6, "国贸": 6, "经济": 6,
    "统计": 6, "数学": 6, "体育": 6, "测绘": 6
}

# 生成学生数据
students = []
student_counter = 1

for college in colleges:
    num_classes_in_college = college_classes[college]
    for major in majors[college]:
        for class_num in range(1, num_classes_in_college // 2 + 1):  # 每个专业的班级数量
            for _ in range(students_per_class):  # 每个班级50个学生
                student_id = generate_student_id("20240001", student_counter)
                students.append({
                    "学院": college,
                    "专业": major,
                    "班级": f"{major}班级{class_num}",
                    "学号": student_id
                })
                student_counter += 1

# 将学生数据保存到DataFrame
df = pd.DataFrame(students)

# 保存到Excel文件
df.to_excel("students_data.xlsx", index=False)

print("学生数据已成功生成并保存到Excel文件")
