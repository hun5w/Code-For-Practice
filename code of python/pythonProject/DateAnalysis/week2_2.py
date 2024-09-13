'''
第二周周五课程 随堂练习
'''

from math import e

index="abc\nde"
print(index[3])
print(index[4])

print("{name} is {age} years old".format(name="wan",age="20"))
print(f"Euler's constant is roughly {e}")

'''
使用四种不同的格式化方法：f-string、format、% 操作符和旧式的 % 格式化。
题目： 假设你是一名教师，需要为学生打印出他们的分数报告。每个学生有一个名字和两个科目的成绩。请使用以下四种不同的字符串格式化方法，为每个学生生成一个分数报告。
学生信息：
•  学生A：名字为 “Alice”，数学成绩为 92，英语成绩为 88
•  学生B：名字为 “Bob”，数学成绩为 75，英语成绩为 85
要求： 使用以下四种格式化方法，为每个学生打印出以下格式的报告：
学生姓名：[名字]，数学成绩：[数学成绩]，英语成绩：[英语成绩]
'''

studentnameA="Alice"
studentnameB="Bob"
score1=92
score2=88
score3=75
score4=85
print(f"student A:name is {studentnameA},the score of math is {score1},thw score of English is {score2}")
print(f"student B:name is {studentnameB},the score of math is {score3},thw score of English is {score4}")

print("Student A:name is {studentnameA},the score of math is {score1},the score of English is {score2}".format(studentnameA="Alice",score1=92,score2=88))
print("Student B:name is {studentnameB},the score of math is {score3},the score of English is {score4}".format(studentnameB="Bob",score3=75,score4=85))

report_a="Student A:name is studentnameA:%s,the score of math is score1%d,the score of English is score2%d"%(studentnameA,score1,score2)
report_b="Student B:name is studentnameB:%s,the score of math is score3%d,the score of English is score4%d"%(studentnameB,score3,score4)

print(report_a)
print(report_b)

