//双链表的初始化
#include <stdio.h>
#include <stdlib.h>

typedef struct DNode {
    int data;
    struct DNode *prev;
    struct DNode *next;
} DNode, *DLinkList;

//双链表的插入
void InsertDLinkList(DLinkList *L, int i, int e) {
    DNode *p = (DNode *)malloc(sizeof(DNode));
    p->data = e;
    if (i == 1) { // 在表头插入
        p->next = *L;
        p->prev = NULL;
        if (*L != NULL) {
            (*L)->prev = p;
        }
        *L = p;
    } else { // 在表中间或表尾插入
        DNode *q = *L;
        for (int j = 1; j < i - 1 && q != NULL; j++) {
            q = q->next;
        }
        if (q != NULL) {
            p->next = q->next;
            p->prev = q;
            if (q->next != NULL) {
                q->next->prev = p;
            }
            q->next = p;
        } else {
            free(p); // 插入位置不合法，释放内存
        }
    }
}

//双链表的删除
void DeleteDLinkList(DLinkList *L, int i) {
    if (*L == NULL) return; // 空链表
    DNode *p = *L;
    for (int j = 1; j < i && p != NULL; j++) {
        p = p->next;
    }
    if (p != NULL) {
        if (p->prev != NULL) {
            p->prev->next = p->next;
        } else {
            *L = p->next; // 删除的是头结点
        }
        if (p->next != NULL) {
            p->next->prev = p->prev;
        }
        free(p);
    }
}

//双链表的遍历
void TraverseDLinkList(DLinkList L) {
    DNode *p = L;
    while (p != NULL) {
        printf("%d ", p->data);
        p = p->next;
    }
    printf("\n");
}
