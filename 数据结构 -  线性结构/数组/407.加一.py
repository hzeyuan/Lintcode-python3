"""
407. 加一
给定一个非负数，表示一个数字数组，在该数的基础上+1，返回一个新的数组。

该数字按照数位高低进行排列，最高位的数在列表的最前面。

样例
给定 [1,2,3] 表示 123, 返回 [1,2,4].

给定 [9,9,9] 表示 999, 返回 [1,0,0,0].
"""


class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    # time:2071 ms
    def plusOne(self, digits):
        # write your code here
        a = ''
        for i in digits:
            a += str(i)
        a = str(int(a) + 1)
        res = []
        for i in list(a):
            res.append(int(i))
        return res
