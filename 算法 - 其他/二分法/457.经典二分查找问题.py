"""
457. 经典二分查找问题
在一个排序数组中找一个数，返回该数出现的任意位置，如果不存在，返回-1

样例
给出数组 [1, 2, 2, 4, 5, 5].

对于 target = 2, 返回 1 或者 2.
对于 target = 5, 返回 4 或者 5.
对于 target = 6, 返回 -1.
"""


class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """
    # time:14257ms
    def findPosition(self, nums, target):
        # write your code here
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                    return mid
        return -1
