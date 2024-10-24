/*
给定数轴X上n个不同点的集合{x1,x2,...,xn},其中x1<x2<...<xn。
现在用若干长度为1的闭区间来覆盖这些点，
设计一个算法找到最少的闭区间个数和位置，输出闭区间位置和个数
*/

#include <stdio.h>

// 找到闭区间的位置和数量
void findIntervals(int point[], int n) {
    int intervals[n];
    int interval_count = 0;
    int i = 0;

    while (i < n) {
        interval_count++;
        int location = point[i] + 1;
        intervals[interval_count - 1] = location;

        // 跳过所有在当前闭区间覆盖范围内的点
        while (i < n && point[i] <= location) {
            i++;
        }
    }

    // 输出闭区间的位置和数量
    printf("闭区间的位置: ");
    for (int j = 0; j < interval_count; j++) {
        printf("%d ", intervals[j]);
    }
    printf("\n闭区间的数量: %d\n", interval_count);
}

int main() {
    int point[] = {2, 4, 5, 7, 9, 10, 12, 14, 15, 17};
    int n = sizeof(point) / sizeof(point[0]);

    findIntervals(point, n);

    return 0;
}