"""
767. 翻转数组
原地翻转给出的数组 nums

样例
给出 nums = [1,2,5]
返回 [5,2,1]
"""


class Solution:
    """
    @param nums: a integer array
    @return: nothing
    """
    # time:403 ms
    def reverseArray(self, nums):
        # write your code here
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
            left += 1


s = Solution()
a = [1, 2, 3, 4, 5]
s.reverseArray(a)
print(a)
