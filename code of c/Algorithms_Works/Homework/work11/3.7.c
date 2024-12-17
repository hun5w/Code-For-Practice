/*在一条直线的公路两旁有n个位置x1，x2，...，xn可以开商店，在位置xi开商店的预期收益是pi，i=1，2，...，n。
如果任何两个商店之间的距离必须至少为d千米，那么如何选择开设商店的位置使得总收益达到最大*/

#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int x; // 位置
    int p; // 收益
} Store;

// 比较函数，用于按位置排序
int compare(const void *a, const void *b) {
    Store *s1 = (Store *)a;
    Store *s2 = (Store *)b;
    return s1->x - s2->x;
}

int max(int a, int b) {
    return a > b ? a : b;
}

void findMaxProfit(Store stores[], int n, int d) {
    // 按位置排序
    qsort(stores, n, sizeof(Store), compare);

    int dp[n];
    dp[0] = stores[0].p;

    for (int i = 1; i < n; i++) {
        dp[i] = stores[i].p;
        for (int j = 0; j < i; j++) {
            if (stores[i].x - stores[j].x >= d) {
                dp[i] = max(dp[i], dp[j] + stores[i].p);
            }
        }
    }

    int maxProfit = 0;
    for (int i = 0; i < n; i++) {
        maxProfit = max(maxProfit, dp[i]);
    }

    printf("最大总收益为 %d\n", maxProfit);
}

int main() {
    // 第一组测试数据
    Store stores1[] = {{1, 5}, {2, 6}, {4, 5}, {6, 8}, {7, 10}};
    int n1 = sizeof(stores1) / sizeof(stores1[0]);
    int d1 = 2;
    printf("第一组测试数据:\n");
    findMaxProfit(stores1, n1, d1);

    // 第二组测试数据
    Store stores2[] = {{1, 3}, {3, 5}, {6, 8}, {7, 9}, {9, 6}};
    int n2 = sizeof(stores2) / sizeof(stores2[0]);
    int d2 = 3;
    printf("\n第二组测试数据:\n");
    findMaxProfit(stores2, n2, d2);

    // 第三组测试数据
    Store stores3[] = {{1, 2}, {2, 4}, {5, 7}, {6, 3}, {8, 9}};
    int n3 = sizeof(stores3) / sizeof(stores3[0]);
    int d3 = 2;
    printf("\n第三组测试数据:\n");
    findMaxProfit(stores3, n3, d3);

    return 0;
}