//子集和问题，设n个不同的正数构成集合S，求出使得和为某数M的S的所有子集（看成 0-1背包问题）

#include <stdio.h>

#define MAX_N 100

void findSubsets(int S[], int subset[], int n, int M, int index, int currentSum, int start) {
    if (currentSum == M) {
        printf("{ ");
        for (int i = 0; i < index; i++) {
            printf("%d ", subset[i]);
        }
        printf("}\n");
        return;
    }
    if (currentSum > M || start == n) {
        return;
    }
    for (int i = start; i < n; i++) {
        subset[index] = S[i];
        findSubsets(S, subset, n, M, index + 1, currentSum + S[i], i + 1);
    }
}

int main() {
    int S[MAX_N], subset[MAX_N];
    int n, M;

    printf("输入集合的大小 n: ");
    scanf("%d", &n);
    printf("输入集合的元素: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &S[i]);
    }
    printf("输入目标和 M: ");
    scanf("%d", &M);

    printf("所有和为 %d 的子集:\n", M);
    findSubsets(S, subset, n, M, 0, 0, 0);

    return 0;
}