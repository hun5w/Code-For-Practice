//静态链表

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAXSIZE 100 // 静态链表的最大长度

typedef struct {
    int data;
    int next; // 下一个元素的下标
} Node, StaticLinkList[MAXSIZE];