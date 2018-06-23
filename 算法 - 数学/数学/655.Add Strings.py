"""
655. Add Strings
以字符串的形式给出两个非负整数 num1 和 num2，返回 num1 和 num2 的和。

样例
给定 num1 = "123"，num2 = "45"
返回 "168"
"""


class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return sum of num1 and num2
    """
    # time:862ms
    def addStrings(self, num1, num2):
        # write your code here
        return str(int(num1) + int(num2))
