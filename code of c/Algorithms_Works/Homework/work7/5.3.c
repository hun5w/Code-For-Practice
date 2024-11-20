/*5.3如图5.16所示，一个4阶Latin方是一个4×4的方格，在它的每个方格内填入1,2,3或4，
并使得每个数字在每行、每列都恰好出现一次.用回溯法求出所有第1行为1,2,3,4的4阶Latin方.
将每个解的第2行至第4行的数字从左到右写成一个序列.
例如，图5.16中的Latin方对应于解<3,4,1,2,4,3,2,1,2,1,4,3>.给出所有可能的4阶Latin方.
*/

#include <stdio.h>
#include <stdbool.h>

#define N 4

void printSolution(int grid[N][N]) {
    for (int i = 1; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%d ", grid[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

bool isSafe(int grid[N][N], int row, int col, int num) {
    for (int x = 0; x < N; x++) {
        if (grid[row][x] == num || grid[x][col] == num) {
            return false;
        }
    }
    return true;
}

bool solveLatinSquare(int grid[N][N], int row, int col) {
    if (row == N) {
        printSolution(grid);
        return true;
    }
    if (col == N) {
        return solveLatinSquare(grid, row + 1, 0);
    }
    if (grid[row][col] != 0) {
        return solveLatinSquare(grid, row, col + 1);
    }
    for (int num = 1; num <= N; num++) {
        if (isSafe(grid, row, col, num)) {
            grid[row][col] = num;
            solveLatinSquare(grid, row, col + 1);
            grid[row][col] = 0;
        }
    }
    return false;
}

int main() {
    int grid[N][N] = {
        {1, 2, 3, 4},
        {0, 0, 0, 0},
        {0, 0, 0, 0},
        {0, 0, 0, 0}
    };

    solveLatinSquare(grid, 1, 0);
    return 0;
}