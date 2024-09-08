/*
给你一个链表的头节点 head ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。

如果链表中存在环 ，则返回 true 。 否则，返回 false 。
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

//快慢指针
bool hasCycle(struct ListNode *head) {
    if(head == NULL || head->next ==NULL){
        return false;
    }
    struct ListNode *slow = head;
    struct ListNode *fast = head->next;
    while(slow!=fast){
        if(fast == NULL || fast->next == NULL){
            return false;
        }
        slow = slow->next;
        fast = fast->next->next;
    }
    return true;
}

//哈希表

//定义哈希表节点结构
struct HashNode{
    struct ListNode *node;
    struct HashNode *next;
}；

//哈希表的大小
#define HASH_SIZE 10000

//哈希函数
unsigned int hash(struct ListNode *node){
    return (unsigned int)(node) % HASH_SIZE;
}

//使用哈希表判断是否有环
bool hasCycle(struct ListNode *head){
    struct HashNode *hashTable[HASH_SIZE] = {NULL}; //定义一个哈希表hashTable，大小为HASH_SIZE，并将所有元素初始化为NULL

    struct ListNode *current  = head; //初始化指针current指向链表头节点head
    while (current != NULL){
        unsigned int index = hash(current);
        struct HashNode *entry = hashTable[index];

        //遍历哈希表，如果当前节点已经在哈希表中，则说明有环
        while(entry !=NULL){
            if(entry->node == current){
                return true;
            }
            entry = entry->next;
        }
        
        //将当前节点加入哈希表
        struct HashNode *newEntry = (struct HashNode *)malloc(sizeof(struct HashNode));
        newEntry->node = current;
        newEntry->next = hashTable[index];
        hashTable[index] = newEntry;

        //指针current指向下一个节点
        current = current->next;

    }
    return false;
}