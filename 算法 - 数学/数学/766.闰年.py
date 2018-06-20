"""
766. 闰年
判断给出的年份 n 是否为闰年. 如果 n 为闰年则返回 true

样例
给出 n = 2008 返回 true
给出 n = 2018 返回 false
"""


class Solution:
    """
    @param n: a number represent year
    @return: whether year n is a leap year.
    """

    # time:1366 ms
    def isLeapYear(self, n):
        # write your code here
        return True if n % 4 == 0 and n % 100 != 0 or n % 400 == 0 else False
