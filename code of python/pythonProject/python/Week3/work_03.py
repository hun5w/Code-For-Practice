'''
str1 = "罚抄"
str2 = "3"
str3 = "遍"
print(str1+str2+str3)
print(str1,str2,str3)

List =[1,2,3,4,5]
print("List[1:4]")
print(List[1:4])
'''

'''
课后作业，60个,姓名+学号+成绩
'''
import random as rm

xing="唐张彭魏徐严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤方"
ming1="家宇能百志航旻浩尊振弘诺远龙寅立伟昀林仕译恺曜晨恺聪宸辉烁诚博玄彦耀伦寅诺江海曜雷海岳迪翰宽博郎"
ming2="祺航西川毅启浩磊郎彦云龙伦航曜翔杉余高远悟浩唯译"

def examination(n):
    Grade = []
    X1 = rm.randint(25,30)
    X2 = rm.randint(15,20)
    X3 = rm.randint(10,15)
    X4 = rm.randint(5,10)
    X5 = rm.randint(3,5)

    while(X1+X2+X3+X4+X5)!=n:
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

    return Grade

def CreateStudent(n,Grade):
    '''
    :Args:
        n:生成学生的数量
    :return:
    '''
    Students=[]
    for i in range(n):
        name=(xing[rm.randint(0,len(xing)-1)]+
              ming1[rm.randint(0,len(ming1)-1)]+
              ming2[rm.randint(0,len(ming2)-1)]
        )
        number=rm.randint(1,60)
        student=[name,f'2022{number:02}',Grade[i]]
        Students.append(student)
    return Students



if __name__=="__main__":
    n=60
    Grade = examination(n)
    Names = CreateStudent(n,Grade)
    print(Names)
