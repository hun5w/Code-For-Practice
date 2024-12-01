/*卫兵布置问题，一个博物馆由排成m*n个矩形阵列的陈列室组成，需要在陈列室中设立哨位，
每个哨位上的哨兵除了可以监视自己所在的陈列室外，还可以监视自己所在陈列室的上下左右4个
陈列室，试给出一个最佳哨位安排方法，使得所有陈列室都在监视之下，但使用的哨兵最少*/

#include <stdio.h>
#include <stdbool.h>

#define M 4
#define N 6

int minGuards;
int bestArrangement[M][N];
int currentArrangement[M][N];
int museum[M][N];

bool isMonitored(int row, int col) {
    if (museum[row][col] == 1) return true;
    if (row > 0 && museum[row - 1][col] == 1) return true;
    if (row < M - 1 && museum[row + 1][col] == 1) return true;
    if (col > 0 && museum[row][col - 1] == 1) return true;
    if (col < N - 1 && museum[row][col + 1] == 1) return true;
    return false;
}

void placeGuards(int row, int col, int guards) {
    if (row == M) {
        // Check if all rooms are monitored
        bool allMonitored = true;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (!isMonitored(i, j)) {
                    allMonitored = false;
                    break;
                }
            }
            if (!allMonitored) break;
        }

        if (allMonitored && guards < minGuards) {
            minGuards = guards;
            for (int i = 0; i < M; i++) {
                for (int j = 0; j < N; j++) {
                    bestArrangement[i][j] = currentArrangement[i][j];
                }
            }
        }
        return;
    }

    if (col == N) {
        placeGuards(row + 1, 0, guards);
        return;
    }

    // Try placing a guard at the current position
    museum[row][col] = 1;
    currentArrangement[row][col] = 1;
    placeGuards(row, col + 1, guards + 1);
    museum[row][col] = 0;
    currentArrangement[row][col] = 0;

    // Try not placing a guard at the current position
    placeGuards(row, col + 1, guards);
}

void printSolution() {
    printf("最少哨兵数量: %d\n", minGuards);
    printf("最佳哨位安排:\n");
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d ", bestArrangement[i][j]);
        }
        printf("\n");
    }
}

void initializeArrays() {
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            bestArrangement[i][j] = 0;
            currentArrangement[i][j] = 0;
            museum[i][j] = 0;
        }
    }
}

int main() {
    minGuards = M * N;
    initializeArrays();

    placeGuards(0, 0, 0);
    printSolution();

    return 0;
}