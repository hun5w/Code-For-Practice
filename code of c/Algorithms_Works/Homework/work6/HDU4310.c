#include <stdio.h>
#include <stdlib.h>

// 定义敌方英雄结构体
typedef struct {
    int dps;
    int hp;
    double ratio;
} Hero;

// 比较函数，用于按 DPS/HP 比值从大到小排序
int compare(const void *a, const void *b) {
    Hero *h1 = (Hero *)a;
    Hero *h2 = (Hero *)b;
    if (h1->ratio > h2->ratio) return -1;
    if (h1->ratio < h2->ratio) return 1;
    return 0;
}

int main() {
    int T;
    scanf("%d", &T);

    while (T--) {
        int N;
        scanf("%d", &N);

        Hero *heroes = (Hero *)malloc(N * sizeof(Hero));
        for (int i = 0; i < N; i++) {
            scanf("%d %d", &heroes[i].dps, &heroes[i].hp);
            heroes[i].ratio = (double)heroes[i].dps / heroes[i].hp;
        }

        // 按 DPS/HP 比值从大到小排序
        qsort(heroes, N, sizeof(Hero), compare);

        int totalDPS = 0;
        int totalHPLoss = 0;

        // 按排序后的顺序依次攻击敌方英雄
        for (int i = 0; i < N; i++) {
            totalHPLoss += totalDPS * heroes[i].hp;
            totalDPS += heroes[i].dps;
        }

        printf("%d\n", totalHPLoss);

        free(heroes);
    }

    return 0;
}