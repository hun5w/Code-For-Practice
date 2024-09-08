//给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

int search(int* nums, int numsSize, int target) {
    int left = 0;
    int right = numsSize -1;
    /*  闭区间写法 [left,right]， left = 0, right = numsSize - 1
        
        左闭右开区间写法 [left,right), left = 0, right = numsSize
        
        开区间写法 (left,right), left = 0, right = numsSize - 1
       
    */
    while(left + 1 < right){
        int mid = left + (right - left) / 2;
        if (nums[mid] == target){
            return mid;
        }else if (nums[mid] > target){
            right = mid;
        }else {
            left = mid;
        }
    } 
    return -1;
}