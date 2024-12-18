/*3.5设有n种不同面值的硬币，第i种硬币的币值是vi：（其中v1=1)，重量是w，i=1.2.….n，
且现在购买某些总价值为y的商品，需要用这些硬币付款，如果每种钱币使用的个数不限，那么如何选择付款的方法使得付出钱币的总重量最轻？
设计一个求解该问题的算法，假设问题的输入实例是：
v1=1,v2=4,v3=6,v4=8,
w1=1,w2=2,w3=4,w4=6
y=12*/

#include <stdio.h>
#include <limits.h>

#define MAX_Y 10000

int min(int a, int b) {
    return a < b ? a : b;
}

void findMinWeight(int v[], int w[], int n, int y) {
    int dp[MAX_Y + 1];
    for (int i = 0; i <= MAX_Y; i++) {
        dp[i] = INT_MAX;
    }
    dp[0] = 0;

    for (int i = 0; i < n; i++) {
        for (int j = v[i]; j <= y; j++) {
            if (dp[j - v[i]] != INT_MAX) {
                dp[j] = min(dp[j], dp[j - v[i]] + w[i]);
            }
        }
    }

    if (dp[y] == INT_MAX) {
        printf("无法凑成总价值为 %d 的商品\n", y);
    } else {
        printf("凑成总价值为 %d 的商品所需的最小总重量为 %d\n", y, dp[y]);
    }
}

int main() {
    // 第一组测试数据
    int v1[] = {1, 4, 6, 8}; // 硬币面值
    int w1[] = {1, 2, 4, 6}; // 硬币重量
    int n1 = sizeof(v1) / sizeof(v1[0]);
    int y1 = 12; // 目标价值
    printf("第一组测试数据:\n");
    findMinWeight(v1, w1, n1, y1);

    // 第二组测试数据
    int v2[] = {1, 3, 5, 7}; // 硬币面值
    int w2[] = {1, 2, 3, 4}; // 硬币重量
    int n2 = sizeof(v2) / sizeof(v2[0]);
    int y2 = 11; // 目标价值
    printf("\n第二组测试数据:\n");
    findMinWeight(v2, w2, n2, y2);

    // 第三组测试数据
    int v3[] = {1, 2, 5, 10}; // 硬币面值
    int w3[] = {1, 1, 2, 5}; // 硬币重量
    int n3 = sizeof(v3) / sizeof(v3[0]);
    int y3 = 18; // 目标价值
    printf("\n第三组测试数据:\n");
    findMinWeight(v3, w3, n3, y3);

    return 0;
}