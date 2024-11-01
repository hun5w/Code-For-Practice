/*有n个进程p1，p2，...,pn，对于i=1，2，...，n，进程pi的开始时间为s[i]，截止时间为d[i],
可以通过监测程序Test来测试正在运行的进程，Test每次测试的时间很短，可以忽略不计，
换句话说，如果Test在时刻t进行测试，那么它将对满足s[i]<=t<=d[i]的所有进程pi同时取得测试数据
假设最早运行的进程开始时刻是0，问：如何安排测试时刻，使得对每个进程至少测试一次，
且Test测试的次数达到最少？给出伪码，分析算法最坏情况下的时间复杂度 */

#include <stdio.h>
#include <stdlib.h>

// 定义进程结构体
typedef struct {
    int start;
    int end;
} Process;

// 比较函数，用于按截止时间排序
int compare(const void *a, const void *b) {
    Process *p1 = (Process *)a;
    Process *p2 = (Process *)b;
    return p1->end - p2->end;
}

// 安排测试时刻的函数
void scheduleTests(Process processes[], int n) {
    // 按截止时间排序
    qsort(processes, n, sizeof(Process), compare);

    // 初始化测试时间列表
    int *testTimes = (int *)malloc(n * sizeof(int));
    int testCount = 0;

    // 遍历所有进程
    for (int i = 0; i < n; i++) {
        // 如果测试时间列表为空或者最后一个测试时间不在当前进程的时间区间内
        if (testCount == 0 || testTimes[testCount - 1] < processes[i].start || testTimes[testCount - 1] > processes[i].end) {
            // 在当前进程的截止时间进行一次测试
            testTimes[testCount++] = processes[i].end;
        }
    }

    // 输出测试时间
    printf("测试次数: %d\n", testCount);
    printf("测试时间: ");
    for (int i = 0; i < testCount; i++) {
        printf("%d ", testTimes[i]);
    }
    printf("\n");

    // 释放内存
    free(testTimes);
}

int main() {
    // 第一组测试数据
    Process processes1[] = {
        {1, 4},
        {2, 6},
        {4, 7},
        {5, 8},
        {7, 9}
    };
    int n1 = sizeof(processes1) / sizeof(processes1[0]);
    printf("第一组测试数据:\n");
    scheduleTests(processes1, n1);

    // 第二组测试数据
    Process processes2[] = {
        {1, 3},
        {2, 5},
        {3, 6},
        {5, 7},
        {6, 8}
    };
    int n2 = sizeof(processes2) / sizeof(processes2[0]);
    printf("\n第二组测试数据:\n");
    scheduleTests(processes2, n2);

    // 第三组测试数据
    Process processes3[] = {
        {1, 2},
        {2, 4},
        {3, 5},
        {4, 6},
        {5, 7}
    };
    int n3 = sizeof(processes3) / sizeof(processes3[0]);
    printf("\n第三组测试数据:\n");
    scheduleTests(processes3, n3);

    return 0;
}