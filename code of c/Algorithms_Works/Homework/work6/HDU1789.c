#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int deadline;
    int penalty;
} Homework;

// 比较函数，用于按减少的分数从大到小排序，如果减少的分数相同，则按截止日期从小到大排序
int compare(const void *a, const void *b) {
    Homework *h1 = (Homework *)a;
    Homework *h2 = (Homework *)b;
    if (h1->penalty != h2->penalty) {
        return h2->penalty - h1->penalty;
    } else {
        return h1->deadline - h2->deadline;
    }
}

int main() {
    int T;
    scanf("%d", &T);

    while (T--) {
        int N;
        scanf("%d", &N);

        Homework homeworks[N];
        for (int i = 0; i < N; i++) {
            scanf("%d", &homeworks[i].deadline);
        }
        for (int i = 0; i < N; i++) {
            scanf("%d", &homeworks[i].penalty);
        }

        // 按减少的分数从大到小排序，如果减少的分数相同，则按截止日期从小到大排序
        qsort(homeworks, N, sizeof(Homework), compare);

        // 初始化一个数组来记录每一天是否已经安排了作业
        int days[N + 1];
        memset(days, 0, sizeof(days));

        int totalPenalty = 0;

        // 遍历排序后的作业列表
        for (int i = 0; i < N; i++) {
            // 尽量在截止日期之前安排作业
            for (int j = homeworks[i].deadline; j > 0; j--) {
                if (!days[j]) {
                    days[j] = 1;
                    break;
                }
                if (j == 1) {
                    totalPenalty += homeworks[i].penalty;
                }
            }
        }

        printf("%d\n", totalPenalty);
    }

    return 0;
}