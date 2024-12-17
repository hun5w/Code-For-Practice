/*在n个底面为长方形的货柜需要租用库房存放。如果每个货柜都必须放在地面上，
且所有货柜的底面宽度都等于库房的宽度，那么第i个货柜占用库房面积大小只需要用
它的底面长度li来表示，i=1，2，...，n，设库房总长度是D（li<=D且li和>D）.
设第i号货柜的仓储收益是Vi，若要求库房出租收益达到最大，问如何选择放入库房
的货柜？若l1，l2，...，ln，D都是正整数，设计一个算法求解这个问题，*/

#include <stdio.h>

#define MAX_N 100
#define MAX_D 1000

int max(int a, int b) {
    return a > b ? a : b;
}

void maximizeStorage(int n, int lengths[], int values[], int D) {
    int dp[MAX_D + 1] = {0};

    for (int i = 0; i < n; i++) {
        for (int j = D; j >= lengths[i]; j--) {
            dp[j] = max(dp[j], dp[j - lengths[i]] + values[i]);
        }
    }

    printf("最大仓储收益: %d\n", dp[D]);
}

int main() {
    // 测试数据1
    int n1 = 5;
    int lengths1[] = {1, 2, 3, 4, 5};
    int values1[] = {10, 20, 30, 40, 50};
    int D1 = 10;
    printf("测试数据1:\n");
    maximizeStorage(n1, lengths1, values1, D1);

    // 测试数据2
    int n2 = 5;
    int lengths2[] = {2, 3, 4, 5, 6};
    int values2[] = {15, 25, 35, 45, 55};
    int D2 = 12;
    printf("测试数据2:\n");
    maximizeStorage(n2, lengths2, values2, D2);

    // 测试数据3
    int n3 = 5;
    int lengths3[] = {1, 3, 4, 5, 7};
    int values3[] = {10, 30, 40, 50, 70};
    int D3 = 15;
    printf("测试数据3:\n");
    maximizeStorage(n3, lengths3, values3, D3);

    return 0;
}