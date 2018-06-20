"""
373. 奇偶分割数组
分割一个整数数组，使得奇数在前偶数在后。

样例
给定 [1, 2, 3, 4]，返回 [1, 3, 2, 4]。

挑战
在原数组中完成，不使用额外空间。
"""


class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    # time:1007ms
    def partitionArray(self, nums):
        # write your code here
        j = 0
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


s = Solution()
a = [1, 2, 3, 4]
s.partitionArray(a)
print(a)
