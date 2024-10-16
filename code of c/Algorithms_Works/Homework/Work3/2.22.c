/*设A={a1,a2,...,an}和B={b1,b2,...,bm}是两个整数集合，其中m=O(logn),
设计算法计算集合C=(A-B)∪(B-A)。说明算法的主要步骤，并以比较作基本运算分析算法最坏情况下的时间复杂度*/

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

// 计算集合的对称差
void symmetricDifference(int A[], int B[], int n, int m) {
    HashTable* hashA = createHashTable();
    HashTable* hashB = createHashTable();
    int* C = (int*)malloc((n + m) * sizeof(int));
    int k = 0;

    // 将集合 A 的元素插入到哈希表 hashA 中
    for (int i = 0; i < n; i++) {
        insertHashTable(hashA, A[i]);
    }

    // 将集合 B 的元素插入到哈希表 hashB 中
    for (int j = 0; j < m; j++) {
        insertHashTable(hashB, B[j]);
    }

    // 计算 A - B
    for (int i = 0; i < n; i++) {
        if (!searchHashTable(hashB, A[i])) {
            C[k++] = A[i];
        }
    }

    // 计算 B - A
    for (int j = 0; j < m; j++) {
        if (!searchHashTable(hashA, B[j])) {
            C[k++] = B[j];
        }
    }

    // 打印结果集合 C
    printf("Symmetric Difference (A - B) ∪ (B - A): ");
    for (int i = 0; i < k; i++) {
        printf("%d ", C[i]);
    }
    printf("\n");

    // 释放内存
    free(C);
    freeHashTable(hashA);
    freeHashTable(hashB);
}

