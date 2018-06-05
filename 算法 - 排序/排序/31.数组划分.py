"""
给出一个整数数组 nums 和一个整数 k。划分数组（即移动数组 nums 中的元素），使得：

所有小于k的元素移到左边
所有大于等于k的元素移到右边
返回数组划分的位置，即数组中第一个位置 i，满足 nums[i] 大于等于 k。

样例
给出数组 nums = [3,2,2,1] 和 k = 2，返回 1.

挑战
使用 O(n) 的时间复杂度在数组上进行划分。
"""


class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    # 快排的第一步
    # time:1050ms
    def partitionArray(self, nums, k):
        # write your code here
        left,right = 0,len(nums)-1
        while left<right:
            while left<right and nums[right] >=k:
                right -=1
            while left<right and nums[left] <k:
                left +=1
            nums[left],nums[right] = nums[right],nums[left]
        if len(nums) == left+1:
            return left+1
        else:
            return left
    """
    # 偷懒点的方法
    # time: 1108ms
    def partitionArray(self, nums, k):
        
        number = 0
        for i in nums:
            if i >= k:
                number += 1
        return len(nums) - number
    """
