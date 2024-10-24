/*
设有一条边缘山区的道路AB，沿着道路AB分布着n所房子，这些房子到A的距离分别是x1,x2,...,xn(x1<x2<...<xn)
为了给所有房子的用户提供电话服务，需要在这条道路上设置一些基站。为了保证通信质量，每所房子应该位于距离某个基站的
4km范围之内，设计一个算法找到基站的位置，并且使得基站的数量尽可能少。  输出基站的位置 和 个数
*/

#include <stdio.h>

// 找到基站的位置和数量
void findStations(int houses[], int n) {
    int stations[n];
    int station_count = 0;
    int i = 0;

    while (i < n) {
        station_count++;
        int location = houses[i] + 4;
        stations[station_count - 1] = location;

        while (i < n && houses[i] <= location + 4) {
            i++;
        }
    }

    // 输出基站的位置和数量
    printf("基站的位置: ");
    for (int j = 0; j < station_count; j++) {
        printf("%d ", stations[j]);
    }
    printf("\n基站的数量: %d\n", station_count);
}

int main() {
    int houses[] = {1, 2, 3, 5, 9, 11, 12, 14, 18, 20};
    int n = sizeof(houses) / sizeof(houses[0]);

    findStations(houses, n);

    return 0;
}