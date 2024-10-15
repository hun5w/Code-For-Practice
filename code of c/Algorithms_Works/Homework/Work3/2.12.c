/*设A={a1,a2,...,an},B={b1,b2,...,bn}是整数集合，其中m=Ologn.
设计一个算法找出集合C=A∩B。要求给出伪码描述*/

#include <stdio.h>
#include <stdlib.h>

// 定义哈希表的大小
#define TABLE_SIZE 100

// 哈希表节点结构
typedef struct HashNode {
    int key;
    struct HashNode* next;
} HashNode;

// 哈希表结构
typedef struct HashTable {
    HashNode* table[TABLE_SIZE];
} HashTable;

// 创建哈希表
HashTable* createHashTable() {
    HashTable* hashTable = (HashTable*)malloc(sizeof(HashTable));
    for (int i = 0; i < TABLE_SIZE; i++) {
        hashTable->table[i] = NULL;
    }
    return hashTable;
}

// 哈希函数
int hashFunction(int key) {
    return key % TABLE_SIZE;
}

// 插入元素到哈希表
void insertHashTable(HashTable* hashTable, int key) {
    int hashIndex = hashFunction(key);
    HashNode* newNode = (HashNode*)malloc(sizeof(HashNode));
    newNode->key = key;
    newNode->next = hashTable->table[hashIndex];
    hashTable->table[hashIndex] = newNode;
}

// 查找元素在哈希表中是否存在
int searchHashTable(HashTable* hashTable, int key) {
    int hashIndex = hashFunction(key);
    HashNode* node = hashTable->table[hashIndex];
    while (node != NULL) {
        if (node->key == key) {
            return 1;
        }
        node = node->next;
    }
    return 0;
}

// 释放哈希表
void freeHashTable(HashTable* hashTable) {
    for (int i = 0; i < TABLE_SIZE; i++) {
        HashNode* node = hashTable->table[i];
        while (node != NULL) {
            HashNode* temp = node;
            node = node->next;
            free(temp);
        }
    }
    free(hashTable);
}

// 查找集合的交集
void findIntersection(int A[], int B[], int n, int m) {
    HashTable* hashTable = createHashTable();
    int* C = (int*)malloc(n * sizeof(int));
    int k = 0;

    // 将集合 A 的元素插入到哈希表中
    for (int i = 0; i < n; i++) {
        insertHashTable(hashTable, A[i]);
    }

    // 查找集合 B 的元素是否在哈希表中
    for (int j = 0; j < m; j++) {
        if (searchHashTable(hashTable, B[j])) {
            C[k++] = B[j];
        }
    }

    // 打印交集结果
    printf("Intersection of A and B: ");
    for (int i = 0; i < k; i++) {
        printf("%d ", C[i]);
    }
    printf("\n");

    // 释放内存
    free(C);
    freeHashTable(hashTable);
}


/*function findIntersection(A, B):
    H = empty hash table
    C = empty set

    for each a in A:
        insert a into H

    for each b in B:
        if b is in H:
            insert b into C

    return C
*/