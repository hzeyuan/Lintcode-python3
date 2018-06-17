"""
41. 最大子数组
给定一个整数数组，找到一个具有最大和的子数组，返回其最大和。

样例
给出数组[−2,2,−3,4,−1,2,1,−5,3]，符合要求的子数组为[4,−1,2,1]，其最大和为6

挑战
要求时间复杂度为O(n)
"""


class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    # 贪心算法
    # time:786 ms
    def maxSubArray(self, nums):
        # write your code here
        ans, sum = -float('inf'), 0
        for i in nums:
            sum += i
            if sum > ans:
                ans = sum
            if sum < 0:
                sum = 0
        return ans


s = Solution()
print(s.maxSubArray([-2, 2, -3, 4, -1, 2, 1, -5, 3]))
