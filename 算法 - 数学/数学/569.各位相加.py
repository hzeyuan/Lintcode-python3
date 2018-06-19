"""
569. 各位相加
给出一个非负整数 num，反复的将所有位上的数字相加，直到得到一个一位的整数。

样例
给出 num = 38。

相加的过程如下：3 + 8 = 11，1 + 1 = 2。因为 2 只剩下一个数字，所以返回 2。

挑战
你可以不用任何的循环或者递归算法，在 O(1) 的时间内解决这个问题么
"""


class Solution:
    """
    @param num: a non-negative integer
    @return: one digit
    """
    # time:1663 ms
    def addDigits(self, num):
        # write your code here
        if num == 0:
            return 0
        else:
            number = num % 9
            if number == 0:
                return 9
            else:
                return number
