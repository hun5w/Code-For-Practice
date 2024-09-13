import random as rm

def getmatrix(n):
    '''

    :param n:
    :return:
    '''

    mat = [[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n):
            mat[i][j] = rm.randint(1,10)
    return mat

def print_matrix(mat):
    '''

    :param mat:
    :return:
    '''
    m=len(mat)
    for i in range(m):
        print(mat[i])

if __name__=="__main__":
    n=int(input("请输入n生成一个n*n的矩阵\n"))
    matl=getmatrix(n)
    print_matrix(matl)