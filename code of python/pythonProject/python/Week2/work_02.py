"""第二周周五课堂作业"""
'''
课堂练习
path=r""
print(path,end="\n")

mypath="python"
print(mypath[1:3])
print(mypath[:-1])
'''

#coding=utf-8
import random as rm

xing="唐张彭魏徐"
ming1="家宇能百志"
ming2="祺航西川毅"

def CreateStudent(n):
    '''

    :Args:
        n:生成学生的数量
    :return:
    '''
    StudentsName=[]
    for i in range(n):
        name=xing[rm.randint(0,len(xing)-1)]+ming1[rm.randint(0,len(ming1)-1)]+ming2[rm.randint(0,len(ming2)-1)]
        number=rm.randint(1,60)
        student=[name,number]
        StudentsName.append(student)
    return StudentsName

def Examination():
    Grade = []
    X1 = rm.randint(25,30)
    X2 = rm.randint(15,20)
    X3 = rm.randint(10,15)
    X4 = rm.randint(5,10)
    X5 = rm.randint(3,5)

    while((X1+X2+X3+X4+X5)!=n):
        X1 = rm.randint(25, 30)
        X2 = rm.randint(15, 20)
        X3 = rm.randint(10, 15)
        X4 = rm.randint(5, 10)
        X5 = rm.randint(3, 5)
    for i in range(X1):
        Grade.append(rm.randint(90,100))
    for i in range(X2):
        Grade.append(rm.randint(80,90))
    for i in range(X3):
        Grade.append(rm.randint(70, 80))
    for i in range(X4):
        Grade.append(rm.randint(60, 70))
    for i in range(X5):
        Grade.append(rm.randint(0, 60))
def Dengfen():
    pass
if __name__=="__main__":
    n=5
    Names = CreateStudent(n)

    print(Names)
