"""
39. 恢复旋转排序数组
给定一个旋转排序数组，在原地恢复其排序。

样例
[4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]

挑战
使用O(1)的额外空间和O(n)时间复杂度
"""


class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    # 每次比较数组第一个数字和最后一个数字
    # time:1065ms
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        while nums:
            if nums[-1] <= nums[0]:
                nums.insert(0, nums.pop())
            else:
                break
