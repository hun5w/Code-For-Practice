/*设S={1，2，...，n}是n项广告的集合，广告i（i=1，2，...，n）有发布时间s（i），截止时间d（i），发布效益是v（i），
其中s（i）是非负整数，d（i）和v（i）是正整数，且d（1）《=d（2）《=...《=d（n），
我们的问题是：如何在S中选择一组广告A，使得A中任意两个广告都相容（时间段不重叠）且总效益最大
假设所有广告效益相等，试设计一个求解上述问题的算法，证明其正确性，并说明时间复杂度*/

#include <stdio.h>

// 定义广告结构体
typedef struct {
    int start_time;
    int end_time;
    int value;
} Ad;

// 选择广告
void selectAds(Ad ads[], int n) {
    Ad selected_ads[n];
    int selected_count = 0;
    int last_end_time = -1;

    for (int i = 0; i < n; i++) {
        if (ads[i].start_time >= last_end_time) {
            selected_ads[selected_count++] = ads[i];
            last_end_time = ads[i].end_time;
        }
    }

    // 输出选择的广告
    printf("选择的广告:\n");
    for (int i = 0; i < selected_count; i++) {
        printf("广告 %d: 开始时间 = %d, 结束时间 = %d, 效益 = %d\n",
               i + 1, selected_ads[i].start_time, selected_ads[i].end_time, selected_ads[i].value);
    }
}

int main() {
    Ad ads[] = {
        {1, 3, 10},
        {2, 5, 10},
        {4, 6, 10},
        {6, 8, 10},
        {5, 9, 10},
        {8, 10, 10},
        {9, 11, 10},
        {11, 13, 10},
        {12, 14, 10},
        {13, 15, 10}
    };
    int n = sizeof(ads) / sizeof(ads[0]);

    selectAds(ads, n);

    return 0;
}