/*分派问题。给n个人分配n件工作，给第i个人分配第j件工作的费用为c[i][j]。
求费用最小的分配方案。*/

#include <stdio.h>
#include <limits.h>

#define N 4

int minCost = INT_MAX;
int bestAssignment[N];
int currentAssignment[N];
int used[N] = {0};

void printSolution() {
    printf("最小费用: %d\n", minCost);
    printf("最佳分配方案: ");
    for (int i = 0; i < N; i++) {
        printf("%d ", bestAssignment[i] + 1);
    }
    printf("\n");
}

void findMinCost(int cost[N][N], int person, int currentCost) {
    if (person == N) {
        if (currentCost < minCost) {
            minCost = currentCost;
            for (int i = 0; i < N; i++) {
                bestAssignment[i] = currentAssignment[i];
            }
        }
        return;
    }

    for (int job = 0; job < N; job++) {
        if (!used[job]) {
            used[job] = 1;
            currentAssignment[person] = job;
            findMinCost(cost, person + 1, currentCost + cost[person][job]);
            used[job] = 0;
        }
    }
}

int main() {
    int cost[N][N] = {
        {10, 3, 2, 7},
        {5, 8, 6, 4},
        {9, 1, 4, 8},
        {6, 7, 5, 3}
    };

    findMinCost(cost, 0, 0);
    printSolution();

    return 0;
}