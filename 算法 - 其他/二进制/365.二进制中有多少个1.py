"""
365. 二进制中有多少个1
计算在一个 32 位的整数的二进制表示中有多少个 1.

样例
给定 32 (100000)，返回 1

给定 5 (101)，返回 2

给定 1023 (1111111111)，返回 10

挑战
If the integer is n bits with m 1 bits. Can you do it in O(m) time?
"""


class Solution:
    """
    @param: num: An integer
    @return: An integer
    """
    # time:775ms
    def countOnes(self, num):
        # write your code here
        binary_number = '{:b}'.format(num) if num >= 0 else '{:b}'.format(2 ** 32 + num)
        one_count = 0
        for i in binary_number:
            if i == '1':
                one_count += 1
        return one_count

    """
    # time:1036 ms
    def countOnes(self, num):
        # write your code here
        count = 0
        num = num if num>=0 else 2**32+num
        while num > 0:
            if num % 2 == 1:
                count += 1
            num //=2
        return count
    """

