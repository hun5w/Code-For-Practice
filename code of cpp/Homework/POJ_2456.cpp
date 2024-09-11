#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;
const int N = 1e6 + 10;
int a[N], n, m;
bool judge(int k) //枚举间距k，看能否把牛全部放完
{
    int cnt = a[0], num = 1;    //num为1表示已经第一头牛放在a[0]牛栏中
    for (int i = 1; i < n; i++) //枚举剩下的牛栏
    {
        if (a[i] - cnt >= k) //a[i]这个牛栏和上一个牛栏间距大于等于k，表示可以再放进牛
        {
            cnt = a[i];
            num++; //又放进了一头牛
        }
        if (num >= m)
            return true; //所有牛都放完了
    }
    return false;
}
int main()
{
    int i;
    while (~scanf("%d%d", &n, &m))
    {
        for (i = 0; i < n; i++)
            scanf("%d", &a[i]);
        sort(a, a + n);                 //对牛栏排序
        int l = 1, r = a[n - 1] - a[0]; //最小距离为1，最大距离为牛栏编号最大的减去编号最小的
        while (l < r)
        {
            int mid = (l + r) >> 1;
            if (judge(mid))
                l = mid + 1;
            else
                r = mid;
        }
        printf("%d\n", r - 1);
    }
    return 0;
}
