/*Problem Description
John has n points on the X axis, and their coordinates are (x[i],0),(i=0,1,2,…,n−1). He wants to know how many pairs<a,b> that |x[b]−x[a]|≤k.(a<b)
 

Input
The first line contains a single integer T (about 5), indicating the number of cases.
Each test case begins with two integers n,k(1≤n≤100000,1≤k≤109).
Next n lines contain an integer x[i](−109≤x[i]≤109), means the X coordinates.
 

Output
For each case, output an integer means how many pairs<a,b> that |x[b]−x[a]|≤k.*/

#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int T;
    printf("请输入测试用例的个数T:\n");
    scanf("%d", &T);
    while (T--) {
        int n, k;
        printf("请输入n和k(用空格分割):\n");
        scanf("%d %d", &n, &k);
        int *x = (int*)malloc(n * sizeof(int)); //动态分配数组
        printf("请输入%d个X坐标(一行一个):\n", n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &x[i]);
        }

        qsort(x, n, sizeof(int), compare); //对x数组进行排序

        long long count = 0;
        int j = 0;
        for (int i = 0; i < n; i++) {
            while (j < n && x[j] - x[i] <= k) {
                j++;
            }
            count += (j - i - 1);
        }

        printf("满足条件的对数为:%lld\n", count);
        free(x); //释放内存
    }
    return 0;
}