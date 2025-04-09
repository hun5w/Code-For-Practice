//单链表的定义

//初始化一个单链表（带头节点）
#include <stdio.h>

bool InitList(LinkList &L) {
    L = (LinkList)malloc(sizeof(LNode)); // 申请头节点
    if (!L) return false; // 申请失败
    L->next = NULL; // 头节点的next指针指向NULL
    return true; // 初始化成功
}

//定义一个单链表
typedef struct LNode {
    int data; // 数据域
    struct LNode *next; // 指针域
} LNode, *LinkList; // LinkList是指向LNode的指针类型
