//给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
//你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。

#include <stdio.h>

//数学方法1.0
int SingleNumber(int* nums,int numsSize){
     int sum1 =0, sum2 = 0;
    for(int i = 0;i < numsSize;i++){
        sum1+= nums[i];
    }
    for(int j = 0;j<numsSize;j++){
        while(nums[j]!=nums[j+1]){
            sum2+=nums[j];
        }
    }
    return 2*sum2-sum1;
}
//超时

//数学方法2.0
int SingleNumber(int* nums,int numsSize){
     int sum1 =0, sum2 = 0;
    for(int i = 0;i < numsSize;i++){
        sum1+= nums[i];
    }
    for(int j = 0;j<numsSize;j++){
      if(j ==0 || nums[j]!=nums[j-1]){
          sum2+=nums[j];
        }
    }
    return 2*sum2-sum1;
}
//程序默认数组元素有序，故输入[4,1,2,1,2]时输出了错误结果
//通过排序后遍历的方法可以解决，但是时间复杂度为O(nlogn)

//哈希表方法


//位运算方法
int SingleNumber(int* nums,int numsSize){
    int ans = 0;
    for(int i = 0;i<numsSize;i++){
        ans^=nums[i];
    }
    return ans;
}
    
