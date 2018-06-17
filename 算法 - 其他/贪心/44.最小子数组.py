"""
44. 最小子数组
给定一个整数数组，找到一个具有最小和的子数组。返回其最小和。

样例
给出数组[1, -1, -2, 1]，返回 -3
"""


class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """
    # 贪心
    # time:1812 ms
    def minSubArray(self, nums):
        # write your code here
        ans, sum = float('inf'), 0
        for i in nums:
            sum += i
            if sum < ans:
                ans = sum
            if sum > 0:
                sum = 0
        return ans
s = Solution()
print(s.minSubArray([ -1, -2, 1]))