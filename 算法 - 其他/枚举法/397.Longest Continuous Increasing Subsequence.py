"""
397. Longest Continuous Increasing Subsequence
给定一个整数数组（下标从 0 到 n-1， n 表示整个数组的规模），请找出该数组中的最长上升连续子序列。（最长上升连续子序列可以定义为从右到左或从左到右的序列。）

样例
给定 [5, 4, 2, 1, 3], 其最长上升连续子序列（LICS）为 [5, 4, 2, 1], 返回 4.

给定 [5, 1, 2, 3, 4], 其最长上升连续子序列（LICS）为 [1, 2, 3, 4], 返回 4.
"""


class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    # 贪心算法
    # time:1037 ms
    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        res = 0
        up = 1
        down = 1
        if len(A) == 1:
            return 1
        for i in range(1, len(A)):
            if A[i] >= A[i - 1]:
                up += 1
                down = 1
            else:
                down += 1
                up = 1
            if up > 1 or down > 1:
                res = max(res, up, down)
        return res


s = Solution()
print(s.longestIncreasingContinuousSubsequence([10]))
