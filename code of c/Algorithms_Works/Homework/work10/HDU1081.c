/*Problem Description
Given a two-dimensional array of positive and negative integers, a sub-rectangle is any contiguous sub-array of size 1 x 1 or greater located within the whole array. The sum of a rectangle is the sum of all the elements in that rectangle. In this problem the sub-rectangle with the largest sum is referred to as the maximal sub-rectangle.

As an example, the maximal sub-rectangle of the array:

0 -2 -7 0
9 2 -6 2
-4 1 -4 1
-1 8 0 -2

is in the lower left corner:

9 2
-4 1
-1 8

and has a sum of 15.
 

Input
The input consists of an N x N array of integers. The input begins with a single positive integer N on a line by itself, indicating the size of the square two-dimensional array. This is followed by N 2 integers separated by whitespace (spaces and newlines). These are the N 2 integers of the array, presented in row-major order. That is, all numbers in the first row, left to right, then all numbers in the second row, left to right, etc. N may be as large as 100. The numbers in the array will be in the range [-127,127].
 

Output
Output the sum of the maximal sub-rectangle.
 

Sample Input
4
0 -2 -7 0 9 2 -6 2
-4 1 -4 1 -1
8 0 -2
 

Sample Output
15*/

#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

// Kadane 算法，用于求解一维数组中的最大子数组和
int kadane(int arr[], int n) {
    int max_sum = INT_MIN;  // 最大子数组和，初始化为最小值
    int current_sum = 0;    // 当前子数组和

    // 遍历数组，计算最大子数组和
    for (int i = 0; i < n; i++) {
        current_sum += arr[i];  // 将当前元素加入当前子数组和
        if (current_sum > max_sum) {
            max_sum = current_sum;  // 更新最大子数组和
        }
        if (current_sum < 0) {
            current_sum = 0;  // 如果当前子数组和小于0，则重置为0，开始新的子数组
        }
    }

    return max_sum;  // 返回最大子数组和
}

int main() {
    int N;
    scanf("%d", &N);  // 输入矩阵的大小

    // 使用动态内存分配来存储矩阵
    int **matrix = (int **)malloc(N * sizeof(int *));
    for (int i = 0; i < N; i++) {
        matrix[i] = (int *)malloc(N * sizeof(int));
    }

    // 读取矩阵数据
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%d", &matrix[i][j]);
        }
    }

    // 变量 max_sum 用来存储最大子矩形的和
    int max_sum = INT_MIN;

    // 临时数组，用来存储两行之间的列累加和
    int *temp = (int *)malloc(N * sizeof(int));

    // 遍历所有可能的行对 (i, j)，i <= j
    for (int i = 0; i < N; i++) {
        // 每次新的 i 都需要重置 temp 数组
        for (int k = 0; k < N; k++) {
            temp[k] = 0;
        }

        // 遍历 j，从 i 到 N
        for (int j = i; j < N; j++) {
            // 更新 temp 数组，将第 j 行的元素累加到 temp 中
            for (int k = 0; k < N; k++) {
                temp[k] += matrix[j][k];
            }

            // 使用 Kadane 算法在 temp 数组中寻找最大子数组和
            int current_sum = kadane(temp, N);

            // 更新最大子矩形的和
            if (current_sum > max_sum) {
                max_sum = current_sum;
            }
        }
    }

    // 输出最大子矩形的和
    printf("%d\n", max_sum);

    // 释放动态分配的内存
    free(temp);
    for (int i = 0; i < N; i++) {
        free(matrix[i]);
    }
    free(matrix);

    return 0;
}
