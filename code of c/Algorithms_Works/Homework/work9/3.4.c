/*设有n项任务，加工时间分别表示为正整数t1，t2，...，tn。现有2台同样的机器，从0时刻
可以安排对这些任务的加工。规定只要有待加工的任务，任何机器就不得闲置。如果直到时刻T所有任务
都完成了，总的加工时间就等于T。设计一个算法找到使得总加工时间T达到最小的调度方案。设
给定实例如下：t1=1，t2=5，t3=2，t4=10，t5=3*/

#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int id;
    int time;
} Task;

int compare(const void *a, const void *b) {
    return ((Task *)b)->time - ((Task *)a)->time;
}

void scheduleTasks(Task tasks[], int n) {
    int machine1 = 0, machine2 = 0;

    printf("任务调度方案:\n");
    for (int i = 0; i < n; i++) {
        if (machine1 <= machine2) {
            printf("任务 %d 分配给机器 1\n", tasks[i].id);
            machine1 += tasks[i].time;
        } else {
            printf("任务 %d 分配给机器 2\n", tasks[i].id);
            machine2 += tasks[i].time;
        }
    }

    int totalTime = machine1 > machine2 ? machine1 : machine2;
    printf("总加工时间: %d\n", totalTime);
}

int main() {
    Task tasks[] = {
    {1, 6},
    {2, 8},
    {3, 5},
    {4, 3},
    {5, 2},
    {6, 4}
};
    int n = sizeof(tasks) / sizeof(tasks[0]);

    qsort(tasks, n, sizeof(Task), compare);
    scheduleTasks(tasks, n);

    return 0;
}