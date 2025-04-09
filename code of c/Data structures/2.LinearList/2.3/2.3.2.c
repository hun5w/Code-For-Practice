//单链表的插入删除

/*按位序插入：在单链表的第i个位置插入一个新结点，找到第i-1个结点，
将新结点的指针域指向第i个结点，将第i-1个结点的指针域指向新结点*/


//在第i个位置插入一个新结点
bool Insert(LinkList &L, int i, int e) {
    LinkList p = L; // p指向头节点
    int j = 0; // j用于计数
    while (p && j < i - 1) { // 找到第i-1个结点
        p = p->next; // p指向下一个结点
        j++; // 计数加1
    }
    if (!p || j > i - 1) return false; // 插入位置不合法，返回false

    LinkList s = (LinkList)malloc(sizeof(LNode)); // 申请新结点s
    s->data = e; // 将数据域赋值为e
    s->next = p->next; // 将新结点的next指针指向第i个结点
    p->next = s; // 将第i-1个结点的next指针指向新结点s
    return true; // 插入成功，返回true
}

//无头节点的单链表插入
bool Insert(LinkList &L, int i, int e) {
    if (i < 1) return false; // 插入位置非法

    if (i == 1) { // 插入第一个节点
        LinkList s = (LinkList)malloc(sizeof(LNode)); // 申请新结点s
        s->data = e; // 将数据域赋值为e
        s->next = L; // 新节点的next指向原链表的第一个节点
        L = s; // 更新头指针，使其指向新节点
        return true;
    }

    LinkList p = L; // p指向头指针
    int j = 1; // j用于计数，从1开始
    while (p && j < i - 1) { // 找到第i-1个结点
        p = p->next; // p指向下一个结点
        j++; // 计数加1
    }
    if (!p || j > i - 1) return false; // 插入位置不合法，返回false

    LinkList s = (LinkList)malloc(sizeof(LNode)); // 申请新结点s
    s->data = e; // 将数据域赋值为e
    s->next = p->next; // 将新结点的next指针指向第i个结点
    p->next = s; // 将第i-1个结点的next指针指向新结点s
    return true; // 插入成功，返回true
}

//结构体的定义
typedef struct Node
{
    int data; //数据域，用来存放数据域；
    struct Node *pNext; //定义一个结构体指针，指向下一次个与当前节点数据类型相同的节点
}NODE,*PNODE;
 
int main()
{
	//struct Node stu1;
	NODE stu1;
	
	//struct Node *a;
	PNODE a = &stu1;
}

//按位查找
LNode * GetElem(LinkList L, int i) {
    if (i < 0) return NULL; // 检查 i 的合法性

    if (i == 0) return L; // 如果 i == 0，返回头节点

    LinkList p = L->next; // p指向第一个有效结点
    int j = 1; // 从第1个有效节点开始计数

    while (p && j < i) { // 找到第i个结点
        p = p->next; // p指向下一个结点
        j++; // 计数加1
    }

    if (!p) return NULL; // 查找失败，返回NULL
    return p; // 返回第i个结点的指针
}

//按值查找
LNode * LocateElem(LinkList L, int e) {
    LinkList p = L->next; // p指向第一个有效结点

    while (p && p->data != e) { // 查找值为e的结点
        p = p->next; // p指向下一个结点
    }

    return p; // 返回查找结果，可能是NULL
}

//求表长
int ListLength(LinkList L) {
    LinkList p;
    int length = 0;

    if (L->next != NULL) { // 有头节点的情况
        p = L->next; // p指向第一个有效结点
    } else { // 无头节点的情况
        p = L; // p直接指向第一个结点
    }

    while (p) { // 遍历链表
        p = p->next; // p指向下一个结点
        length++; // 长度加1
    }

    return length; // 返回链表的长度
}

//尾插法创建单链表
LinkList CreateListTail(LinkList &L, int n) {
    L = (LinkList)malloc(sizeof(LNode)); // 申请头节点
    if (!L) return NULL; // 申请失败，返回NULL
    L->next = NULL; // 头节点的next指针指向NULL

    LinkList p = L; // p指向头节点
    for (int i = 0; i < n; i++) { // 循环n次
        LinkList s = (LinkList)malloc(sizeof(LNode)); // 申请新结点s
        scanf("%d", &s->data); // 输入数据
        s->next = NULL; // 新结点的next指针指向NULL

        p->next = s; // 将新结点链接到链表中
        p = s; // p指向新结点
    }

    return L; // 返回创建好的链表
}

//头插法创建单链表
LinkList CreateListHead(LinkList &L, int n) {
    L = (LinkList)malloc(sizeof(LNode)); // 申请头节点
    if (!L) return NULL; // 申请失败，返回NULL
    L->next = NULL; // 头节点的next指针指向NULL

    for (int i = 0; i < n; i++) { // 循环n次
        LinkList s = (LinkList)malloc(sizeof(LNode)); // 申请新结点s
        scanf("%d", &s->data); // 输入数据
        s->next = L->next; // 新结点的next指针指向原链表的第一个结点
        L->next = s; // 将新结点链接到链表中
    }

    return L; // 返回创建好的链表
}

//链表的逆置
void ReverseList(LinkList &L) {
    LinkList prev = NULL; // 前驱指针
    LinkList curr = L->next; // 当前指针，指向第一个有效结点
    LinkList next; // 后继指针

    while (curr) { // 遍历链表
        next = curr->next; // 保存后继结点
        curr->next = prev; // 逆置当前结点的指针
        prev = curr; // 前驱指针向前移动
        curr = next; // 当前指针向前移动
    }

    L->next = prev; // 更新头节点的next指针
}