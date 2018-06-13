"""
14. 二分查找
给定一个排序的整数数组（升序）和一个要查找的整数target，用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1。

样例
在数组 [1, 2, 3, 3, 4, 5, 10] 中二分查找3，返回2。

挑战
如果数组中的整数个数超过了2^32，你的算法是否会出错？
"""


class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """

    # time:853ms
    def binarySearch(self, nums, target):
        # write your code here
        left,right = 0,len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = (left + right) // 2 +1
            elif target < nums[mid]:
                right = (left + right) // 2 -1
            else:
                for i in range(left, right + 1):
                    if nums[i] == target:
                        return i
        return -1
