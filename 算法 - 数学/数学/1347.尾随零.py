"""
1347. 尾随零
给定一个整数n，返回n!（n的阶乘）的尾随零的个数。
"""


class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    # time:1006ms
    def trailingZeroes(self, n):
        # write your code here
        count = 0
        while n:
            n //= 5
            count += n
        return count


