/*Problem Description
FatMouse believes that the fatter a mouse is, the faster it runs. To disprove this, you want to take the data on a collection of mice and put as large a subset of this data as possible into a sequence so that the weights are increasing, but the speeds are decreasing.

Input
Input contains data for a bunch of mice, one mouse per line, terminated by end of file.
The data for a particular mouse will consist of a pair of integers: the first representing its size in grams and the second representing its speed in centimeters per second. Both integers are between 1 and 10000. The data in each test case will contain information for at most 1000 mice.
Two mice may have the same weight, the same speed, or even the same weight and speed. 

Output
Your program should output a sequence of lines of data; the first line should contain a number n; the remaining n lines should each contain a single positive integer (each one representing a mouse). If these n integers are m[1], m[2],..., m[n] then it must be the case that 
W[m[1]] < W[m[2]] < ... < W[m[n]]
and 
S[m[1]] > S[m[2]] > ... > S[m[n]]
In order for the answer to be correct, n should be as large as possible.
All inequalities are strict: weights must be strictly increasing, and speeds must be strictly decreasing. There may be many correct outputs for a given input, your program only needs to find one. 

Sample Input
6008 1300
6000 2100
500 2000
1000 4000
1100 3000
6000 2000
8000 1400
6000 1200
2000 1900

Sample Output
4
4
5
9
7
*/

#include <stdio.h>
#include <stdlib.h>

// 定义老鼠数据结构
typedef struct {
    int weight;  // 体重
    int speed;   // 速度
    int index;   // 老鼠的原始索引（1-based）
} Mouse;

// 排序函数，先按体重升序，体重相同则按速度降序
int compare(const void *a, const void *b) {
    Mouse *mouse1 = (Mouse *)a;
    Mouse *mouse2 = (Mouse *)b;
    
    if (mouse1->weight == mouse2->weight) {
        return mouse2->speed - mouse1->speed;  // 速度降序
    }
    return mouse1->weight - mouse2->weight;  // 体重升序
}

int main() {
    // 假设数据量不超过MAX_N
    #define MAX_N 1000

    // 定义测试数据
    Mouse testData[5][MAX_N] = {
        // 测试数据 1
        {
            {6008, 1300, 1}, {6000, 2100, 2}, {500, 2000, 3}, {1000, 4000, 4}, {1100, 3000, 5},
            {6000, 2000, 6}, {8000, 1400, 7}, {6000, 1200, 8}, {2000, 1900, 9}
        },
        // 测试数据 2
        {
            {1000, 3000, 1}, {2000, 2500, 2}, {1500, 2800, 3}, {1800, 2600, 4}, {3000, 2400, 5},
            {2500, 2200, 6}, {4000, 2100, 7}, {3500, 2300, 8}
        },
        // 测试数据 3
        {
            {500, 5000, 1}, {600, 4800, 2}, {700, 4600, 3}, {800, 4400, 4}, {900, 4200, 5},
            {1000, 4000, 6}, {0, 3800, 7}, {1100, 3700, 8}, {1200, 3600, 9}
        },
        // 测试数据 4
        {
            {800, 5000, 1}, {700, 4800, 2}, {600, 4600, 3}, {500, 4400, 4}, {400, 4200, 5},
            {300, 4000, 6}
        },
        // 测试数据 5
        {
            {1200, 2000, 1}, {1500, 1800, 2}, {1000, 2100, 3}, {1300, 1900, 4}, {1700, 1600, 5},
            {1600, 1500, 6}, {1800, 1400, 7}
        }
    };

    // 处理每组数据
    for (int t = 0; t < 5; t++) {
        printf("Test Set %d:\n", t + 1);

        // 获取当前组的数据
        Mouse mice[MAX_N];
        int n = 0;
        while (testData[t][n].weight != 0) {
            mice[n] = testData[t][n];
            n++;
        }

        // 按照体重升序，速度降序排序
        qsort(mice, n, sizeof(Mouse), compare);

        // 动态规划算法计算最长递减子序列
        int *dp = (int *)malloc(n * sizeof(int));  // 动态分配dp数组
        int *prev = (int *)malloc(n * sizeof(int));  // 动态分配prev数组

        if (dp == NULL || prev == NULL) {
            printf("Memory allocation failed!\n");
            return -1; // 如果内存分配失败，返回错误
        }

        // 初始化
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
            prev[i] = -1;
        }

        // 动态规划过程
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (mice[i].speed < mice[j].speed) {
                    if (dp[i] < dp[j] + 1) {
                        dp[i] = dp[j] + 1;
                        prev[i] = j;
                    }
                }
            }
        }

        // 查找最长递减子序列的长度
        int max_len = 0;
        int idx = -1;
        for (int i = 0; i < n; i++) {
            if (dp[i] > max_len) {
                max_len = dp[i];
                idx = i;
            }
        }

        // 回溯并输出最长递减子序列的索引
        int *result = (int *)malloc(max_len * sizeof(int));  // 动态分配结果数组
        int count = max_len - 1;
        while (idx != -1) {
            result[count--] = mice[idx].index;
            idx = prev[idx];
        }

        // 输出结果
        printf("%d\n", max_len);
        for (int i = 0; i < max_len; i++) {
            printf("%d\n", result[i]);
        }

        // 释放动态分配的内存
        free(dp);
        free(prev);
        free(result);

        printf("\n");
    }

    return 0;
}
