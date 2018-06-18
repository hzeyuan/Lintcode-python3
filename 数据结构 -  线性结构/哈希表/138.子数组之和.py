"""
138. 子数组之和
给定一个整数数组，找到和为零的子数组。你的代码应该返回满足要求的子数组的起始位置和结束位置

样例
给出 [-3, 1, 2, -3, 4]，返回[0, 2] 或者 [1, 3].
"""


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    # time:1440 ms
    def subarraySum(self, nums):
        # write your code here
        # 记录nums[i]==0和count = 0的情况
        haxi = {0: -1}
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count in haxi:
                return [haxi[count] + 1, i]
            else:
                haxi[count] = i


s = Solution()
print(s.subarraySum([0]))
