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
        student=[name,f'2022{number:02}']
        StudentsName.append(student)
    return StudentsName

def Examination():
    pass
def Dengfen():
    pass
if __name__=="__main__":
    n=5
    Names = CreateStudent(n)

    print(Names,end="\n")
