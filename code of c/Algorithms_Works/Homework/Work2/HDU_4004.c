/*
The annual Games in frogs' kingdom started again. The most famous game is the Ironfrog Triathlon. 
One test in the Ironfrog Triathlon is jumping. This project requires the frog athletes to jump over the river. 
The width of the river is L (1<= L <= 1000000000). 
There are n (0<= n <= 500000) stones lined up in a straight line from one side to the other side of the river. 
The frogs can only jump through the river, but they can land on the stones. 
If they fall into the river, theyare out. The frogs was asked to jump at most m (1<= m <= n+1) times. 
Now the frogs want to know if they want to jump across the river, at least what ability should they have. 
(That is the frog's longest jump distance).

input
The input contains several cases. The first line of each case contains three positive integer L, n, and m.
Then n lines follow. Each stands for the distance from the starting banks to the nth stone, two stone appear in one place is impossible.
*/
#include<stdio.h>
#include<stdlib.h>
#include<math.h>

//判断是否能跳过
int canCross(int *stones, int n, int L, double m, int maxJump){
    int jumps = 0, lastPostion = 0;
    for(int i = 0; i< n; i++){
        if(stones[i] - lastPostion > maxJump){
            jumps++;
            lastPostion = stones[i-1];
            if(stones[i]-lastPostion > maxJump){
                return 0;
            }
        }
    }
    jumps++;
    return jumps <= m; //返回是否能跳过
}

//比较函数，用于qsort排序
int compare(const void *a,const void *b){
    return *(int *)a - *(int *)b;
}

int main(){
    int T;
    scanf("%d", &T); 

    while(T--){
    int L, n, m; //L为河的长度，n为石头的数量，m为最多跳的次数
    while(scanf("%d %d %d", &L, &n, &m)!=EOF){
        int stones[n+1];//石头的位置
        for(int i = 0; i < n; i++){
            scanf("%d", &stones[i]); //输入石头的位置
        }
        stones[n] = L; //最后一个石头的位置为河的长度
        qsort(stones, n, sizeof(int), compare); //排序

        int low = 1, high = L, result = L; //二分查找
        while(low <= high){
            int mid = (low + high)/2;
            if(canCross(stones, n, L, m, mid)){
                result = mid;
                high = mid -1;
        }else{
            low = mid +1;
            }
        }
            printf("%d\n", result);//输出当前最大跳跃距离    
    }
    }
    return 0;
}
