"""
517. 丑数
写一个程序来检测一个整数是不是丑数。

丑数的定义是，只包含质因子 2, 3, 5 的正整数。比如 6, 8 就是丑数，但是 14 不是丑数以为他包含了质因子 7。

样例
给出 num = 8，返回 true。
给出 num = 14，返回 false。
"""


class Solution:
    """
    @param num: An integer
    @return: true if num is an ugly number or false
    """

    # time:1726 ms
    def isUgly(self, num):
        if num <= 0:
            return False
        while num >= 2 and num % 2 == 0:
            num /= 2
        while num >= 3 and num % 3 == 0:
            num /= 3
        while num >= 5 and num % 5 == 0:
            num /= 5

        return num == 1
