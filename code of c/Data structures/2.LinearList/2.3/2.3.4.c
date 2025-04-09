//循环单链表

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node, *CLinkList;

bool InitCLinkList(CLinkList *L) {
    *L = (CLinkList)malloc(sizeof(Node));
    if (*L == NULL) return false;
    (*L)->next = *L; // 头结点指向自己
    return true;
}

//循环双链表
typedef struct DNode {
    int data;
    struct DNode *prev;
    struct DNode *next;
} DNode, *DLinkList;

bool InitDLinkList(DLinkList *L) {
    *L = (DLinkList)malloc(sizeof(DNode));
    if (*L == NULL) return false;
    (*L)->next = *L; // 头结点指向自己
    (*L)->prev = *L; // 头结点指向自己
    return true;
}