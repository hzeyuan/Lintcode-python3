"""
977. Base 7
Given an integer, return its base 7 string representation.

样例
Given num = 100, return "202".

Given num = -7, return "-10".
"""


class Solution:
    """
    @param num: the given number
    @return: The base 7 string representation
    """
    # time:737 ms
    def convertToBase7(self, num):
        # Write your code here
        s = ''
        is_negative = False
        if num < 0:
            num = -num
            is_negative = True
        while num != 0:
            s += str(num % 7)
            num //= 7
        return s[::-1] if is_negative is False else '-' + s[::-1]
print('8'in '128')