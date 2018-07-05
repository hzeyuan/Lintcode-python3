"""
730. 所有子集的和
给一整数 n, 我们需要求前n个自然数形成的集合的所有可能子集中所有元素的和。

样例
给出 n = 2, 返回 6
可能的子集为 {{1}, {2}, {1, 2}}.
子集的元素和为 1 + 2 + 1 + 2 = 6

给出 n = 3, 返回 24
可能的子集为 {{1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
子集的和为:
1 + 2 + 3 + (1 + 2) + (1 + 3) + (2 + 3) + (1 + 2 + 3) = 24
"""


class Solution:
    """
    @param n: the given number
    @return: Sum of elements in subsets
    """
    # time:715 ms
    # 每个数字出现的次数为2**n-1次方
    def subSum(self, n):
        # write your code here
        res = 0
        for i in range(1, n + 1):
            res += i * 2 ** (n - 1)
        return res


s = Solution()
print(s.subSum(3))
