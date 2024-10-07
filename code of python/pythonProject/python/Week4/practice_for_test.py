'''
期中考试评估分析
已知某班有60个同学选修了三门课程，成绩满足：
总成绩 ()=课程1()+课程2()+ 课程3()。需要写一个函数，CreateRandomNum()，其随机生成k个人的数据，并返回k个人的考试成绩。
a,b,c需要满足的条件，以为例子说明：
（1）任意一个a都是整数，且有下届m1和上届n1; ;比如：；设：m1=20，n1=26；
(2) 这k个数a的平均值为Average1,同样Average需要满足：m1<=Average1<=n1
(3) 这k个的标准方差为p1；;
各门成绩的难度系数不一样A1,A2,A3，p1，p2，p3都不一样。
需要满足的条件：
(1) di=ai+bi+ci
(2)这k个的方差为p4,p4值为给定的值。
题目：
（1）模拟生成班上同学；
（2）写出求平均值的函数
（3）写出求方差的函数
（4）模拟生成各门成绩，并且满足上面各个条件；
（5）统计各个同学的分数
（6）统计某门课程各个分数段的人数
为了更好的反应学生学习的情况，某门课程在期中考试前，且在第一次考试后（第一次考试时间为2022年4月1号），随机对每个同学测试了3次（第一次随机测试与一次考试时间差为第一次随机测试的时间间隔），每次测试时间不一样，间隔天数为：52-60天。现在需要详细的将三次测试成绩显示出来。

（8）写一个测试时间函数，满足52-60天；
（9）写一个姓名生成函数，连续3个成绩排列
（10）生成学生随机测试表，需要写一个测试时间。
'''

import random
import numpy as np


#
def CreateRandomNum(k, m, n, average, std_dev):
    """
    生成k个随机数，满足给定的平均值和标准方差
    :param k: 生成的随机数个数
    :param m: 随机数的下界
    :param n: 随机数的上界
    :param average: 随机数的平均值
    :param std_dev: 随机数的标准方差
    :return: 生成的随机数列表
    """
    while True:
        numbers = [random.randint(m, n) for _ in range(k)]
        if abs(np.mean(numbers) - average) < 0.1 and abs(np.std(numbers) - std_dev) < 0.1:
            return numbers


def CalculateAverage(scores):
    """
    计算平均值
    :param scores: 分数列表
    :return: 平均值
    """
    return np.mean(scores)


def CalculateVariance(scores):
    """
    计算方差
    :param scores: 分数列表
    :return: 方差
    """
    return np.var(scores)


def GenerateScores(k, m1, n1, avg1, d1, m2, n2, avg2, d2, m3, n3, avg3, d3):
    """
    生成三门课程的成绩，并计算总成绩
    :param k: 学生人数
    :param m1, n1, avg1, d1: 课程1的参数
    :param m2, n2, avg2, d2: 课程2的参数
    :param m3, n3, avg3, d3: 课程3的参数
    :return: 三门课程的成绩和总成绩
    """
    course1 = CreateRandomNum(k, m1, n1, avg1, d1)
    course2 = CreateRandomNum(k, m2, n2, avg2, d2)
    course3 = CreateRandomNum(k, m3, n3, avg3, d3)
    total_scores = [course1[i] + course2[i] + course3[i] for i in range(k)]
    return course1, course2, course3, total_scores


def Statistics(scores):
    """
    统计分数的平均值和方差
    :param scores: 分数列表
    :return: 平均值和方差
    """
    return {
        'average': CalculateAverage(scores),
        'variance': CalculateVariance(scores)
    }


def ScoreDistribution(scores):
    """
    统计分数段的人数
    :param scores: 分数列表
    :return: 分数段分布
    """
    distribution = [0] * 11
    for score in scores:
        distribution[score // 10] += 1
    return distribution


if __name__ == "__main__":
    k = 60
    m1, n1, avg1, d1 = 20, 26, 23, 2
    m2, n2, avg2, d2 = 30, 36, 33, 3
    m3, n3, avg3, d3 = 40, 46, 43, 4

    course1, course2, course3, total_scores = \
        (GenerateScores(k, m1, n1, avg1, d1, m2, n2, avg2, d2, m3, n3, avg3,d3))

    print("各门课程成绩统计:")
    print("课程1:", Statistics(course1))
    print("课程2:", Statistics(course2))
    print("课程3:", Statistics(course3))
    print("总成绩:", Statistics(total_scores))

    print("\n课程1分数段分布:")
    distribution = ScoreDistribution(course1)
    for i in range(11):
        print(f"{i * 10}-{i * 10 + 9}: {distribution[i]}人")

    print("\n课程2分数段分布:")
    distribution = ScoreDistribution(course2)
    for i in range(11):
        print(f"{i * 10}-{i * 10 + 9}: {distribution[i]}人")

    print("\n课程3分数段分布:")
    distribution = ScoreDistribution(course3)
    for i in range(11):
        print(f"{i * 10}-{i * 10 + 9}: {distribution[i]}人")