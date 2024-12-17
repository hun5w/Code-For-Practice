/*设A={a1,a2,。。。,an}是正整数的集合，ai的和为n，设计一个算法判断是否能够把A划分成两个子集A1和A2，
使得A1中的数之和与A2中的数之和相等，要求使用一维数组*/

#include <stdio.h>
#include <stdbool.h>

bool canPartition(int A[], int n, int subset1[], int *subset1Size, int subset2[], int *subset2Size) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += A[i];
    }

    // 如果总和是奇数，无法划分成两个和相等的子集
    if (sum % 2 != 0) {
        return false;
    }

    int target = sum / 2;
    bool dp[target + 1];
    int prev[target + 1];
    for (int i = 0; i <= target; i++) {
        dp[i] = false;
        prev[i] = -1;
    }
    dp[0] = true;

    for (int i = 0; i < n; i++) {
        for (int j = target; j >= A[i]; j--) {
            if (dp[j - A[i]]) {
                dp[j] = true;
                prev[j] = i;
            }
        }
    }

    if (!dp[target]) {
        return false;
    }

    // 记录划分结果
    int t = target;
    bool used[n];
    for (int i = 0; i < n; i++) {
        used[i] = false;
    }
    while (t > 0) {
        int i = prev[t];
        subset1[(*subset1Size)++] = A[i];
        used[i] = true;
        t -= A[i];
    }
    for (int i = 0; i < n; i++) {
        if (!used[i]) {
            subset2[(*subset2Size)++] = A[i];
        }
    }

    return true;
}

void printSubset(int subset[], int size) {
    printf("{ ");
    for (int i = 0; i < size; i++) {
        printf("%d ", subset[i]);
    }
    printf("}\n");
}

int main() {
    // 测试数据1
    int A1[] = {1, 5, 11, 5};
    int n1 = sizeof(A1) / sizeof(A1[0]);
    int subset1_1[n1], subset2_1[n1];
    int subset1Size_1 = 0, subset2Size_1 = 0;
    if (canPartition(A1, n1, subset1_1, &subset1Size_1, subset2_1, &subset2Size_1)) {
        printf("测试数据1: 可以将集合划分成两个和相等的子集\n");
        printf("子集1: ");
        printSubset(subset1_1, subset1Size_1);
        printf("子集2: ");
        printSubset(subset2_1, subset2Size_1);
    } else {
        printf("测试数据1: 无法将集合划分成两个和相等的子集\n");
    }

    // 测试数据2
    int A2[] = {1, 2, 3, 5};
    int n2 = sizeof(A2) / sizeof(A2[0]);
    int subset1_2[n2], subset2_2[n2];
    int subset1Size_2 = 0, subset2Size_2 = 0;
    if (canPartition(A2, n2, subset1_2, &subset1Size_2, subset2_2, &subset2Size_2)) {
        printf("测试数据2: 可以将集合划分成两个和相等的子集\n");
        printf("子集1: ");
        printSubset(subset1_2, subset1Size_2);
        printf("子集2: ");
        printSubset(subset2_2, subset2Size_2);
    } else {
        printf("测试数据2: 无法将集合划分成两个和相等的子集\n");
    }

    // 测试数据3
    int A3[] = {3, 1, 1, 2, 2, 1};
    int n3 = sizeof(A3) / sizeof(A3[0]);
    int subset1_3[n3], subset2_3[n3];
    int subset1Size_3 = 0, subset2Size_3 = 0;
    if (canPartition(A3, n3, subset1_3, &subset1Size_3, subset2_3, &subset2Size_3)) {
        printf("测试数据3: 可以将集合划分成两个和相等的子集\n");
        printf("子集1: ");
        printSubset(subset1_3, subset1Size_3);
        printf("子集2: ");
        printSubset(subset2_3, subset2Size_3);
    } else {
        printf("测试数据3: 无法将集合划分成两个和相等的子集\n");
    }

    return 0;
}