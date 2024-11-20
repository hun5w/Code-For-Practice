//3X1+4X2+2X3<=12,求不等式的所有非负整数解

#include <stdio.h>

#define MAX_SUM 12

void backtrack(int X1, int X2, int X3, int sum) {
    if (sum > MAX_SUM) {
        return;
    }
    if (sum <= MAX_SUM) {
        printf("X1 = %d, X2 = %d, X3 = %d\n", X1, X2, X3);
    }
    if (3 * (X1 + 1) + 4 * X2 + 2 * X3 <= MAX_SUM) {
        backtrack(X1 + 1, X2, X3, sum + 3);
    }
    if (3 * X1 + 4 * (X2 + 1) + 2 * X3 <= MAX_SUM) {
        backtrack(X1, X2 + 1, X3, sum + 4);
    }
    if (3 * X1 + 4 * X2 + 2 * (X3 + 1) <= MAX_SUM) {
        backtrack(X1, X2, X3 + 1, sum + 2);
    }
}

int main() {
    backtrack(0, 0, 0, 0);
    return 0;
}