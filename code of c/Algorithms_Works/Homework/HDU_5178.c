/*Problem Description
John has n points on the X axis, and their coordinates are (x[i],0),(i=0,1,2,…,n−1). He wants to know how many pairs<a,b> that |x[b]−x[a]|≤k.(a<b)
 

Input
The first line contains a single integer T (about 5), indicating the number of cases.
Each test case begins with two integers n,k(1≤n≤100000,1≤k≤109).
Next n lines contain an integer x[i](−109≤x[i]≤109), means the X coordinates.
 

Output
For each case, output an integer means how many pairs<a,b> that |x[b]−x[a]|≤k.*/

#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int n, k;
        scanf("%d %d", &n, &k);
        int x[n];
        for (int i = 0; i < n; i++) {
            scanf("%d", &x[i]);
        }

        qsort(x, n, sizeof(int), compare);

        long long count = 0;
        int j = 0;
        for (int i = 0; i < n; i++) {
            while (j < n && x[j] - x[i] <= k) {
                j++;
            }
            count += (j - i - 1);
        }

        printf("%lld\n", count);
    }
    return 0;
}