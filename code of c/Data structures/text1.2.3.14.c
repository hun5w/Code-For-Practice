#include<stdio.h>
int main(void){
    int i = 0, sum = 0;
    int n = 10;
    while(sum<n){
        sum += ++i;
        
        printf("%d \n",sum);
    }
}
