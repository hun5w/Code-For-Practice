/*农夫 John 建造了一座很长的畜栏，它包括N (2 <= N <= 100,000)个隔间，这些小隔间依次编号为x1,...,xN (0 <= xi <= 1,000,000,000). 
但是，John的X (2 <= X <= N)头牛们并不喜欢这种布局，而且几头牛放在一个隔间里，他们就要发生争斗。
为了不让牛互相伤害。John决定自己给牛分配隔间，使任意两头牛之间的最小距离尽可能的大，那么，这个最大的最小距离是什么呢？ 
第一行：空格分隔的两个整数N和X 
第二行——第N+1行：分别指出了xi的位置Output每组测试数据输出一个整数，满足题意的最大的最小值，注意换行。
*/
#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int canPlaceCows(int positions[], int n, int cows, int minDist) {
    int count = 1;
    int lastPosition = positions[0];
    for (int i = 1; i < n; i++) {
        if (positions[i] - lastPosition >= minDist) {
            count++;
            lastPosition = positions[i];
            if (count >= cows) {
                return 1;
            }
        }
    }
    return 0;
}

int main() {
    int n, x;
    printf("请输入隔间数N和牛数X(用空格分割):\n");
    scanf("%d %d", &n, &x);
    int positions[n];
    printf("请输入%d个隔间的位置(一行一个):\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &positions[i]);
    }

    qsort(positions, n, sizeof(int), compare);

    int left = 1, right = positions[n-1] - positions[0];
    int result = 0;

    while (left <= right) {
        int mid = (left + right) / 2;
        if (canPlaceCows(positions, n, x, mid)) {
            result = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    printf("最大的最小距离是:%d\n", result);
    return 0;
}