/*
My birthday is coming up and traditionally I'm serving pie. Not just one pie, no, I have a number N of them, of various tastes and of various sizes. 
F of my friends are coming to my party and each of them gets a piece of pie. 
This should be one piece of one pie, not several small pieces since that looks messy. This piece can be one whole pie though.

My friends are very annoying and if one of them gets a bigger piece than the others, they start complaining. 
Therefore all of them should get equally sized (but not necessarily equally shaped) pieces, 
even if this leads to some pie getting spoiled (which is better than spoiling the party). 
Of course, I want a piece of pie for myself too, and that piece should also be of the same size.

What is the largest possible piece size all of us can get? 
All the pies are cylindrical in shape and they all have the same height 1, 
but the radii of the pies can be different.

Input
One line with a positive integer: the number of test cases. Then for each test case:
---One line with two integers N and F with 1 <= N, F <= 10 000: the number of pies and the number of friends.
---One line with N integers ri with 1 <= ri <= 10 000: the radii of the pies.

*/



#include <stdio.h>
#include <math.h>

#define PI 3.141593

int canDivide(double mid, int N, int F, double r[]){
    int count = 0;
    for(int i = 0; i < N; i++){ //检查每个pie能分多少份
        count += (int)(PI * r[i] *r[i]/mid);
    }
    return count >= F+1;//检查是否能分给每个人一份
}

int main(){
    int T;
    scanf("%d", &T); //输入测试用例数
    while(T--){  //循环读取每个测试用例
        int N, F;
        scanf("%d %d",&N ,&F);
        double r[N];
        for(int i = 0; i< N; i++){
        scanf("%lf", &r[i]);
        }  
    double left = 0, right = 100000000; //初始化左右边界,右边界为面积最大值
    for(int i = 0; i < 100; i++){ //迭代100次，使数据精确到0.0001
        double mid = (left + right)/2;
        if(canDivide(mid, N, F, r)){
            left = mid; //如果能分，说明mid太小，将左边界移到mid
        }else{
            right = mid; //如果不能分，说明mid太大，将右边界移到mid
            }
        }
        printf("%.4f\n", left);   
    }
    return 0;
}        

