"""
37. 反转一个3位整数
反转一个只有3位数的整数。

样例
123 反转之后是 321。
900 反转之后是 9。
"""


class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    # time:286 ms
    def reverseInteger(self, number):
        # write your code here
        if 100 > number > 1000:
            return False
        else:
            bai = number // 100
            shi = number // 10 % 10
            ge = number % 10
            return ge * 100 + shi * 10 + bai
