"""
413. 反转整数
将一个整数中的数字进行颠倒，当颠倒后的整数溢出时，返回 0 (标记为 32 位整数)。

样例
给定 x = 123，返回 321

给定 x = -123，返回 -321
"""


# 三元运算符：#方法一：为真时的结果 if 判定条件 else 为假时的结果
# 方法二：判定条件 and 为真时的结果 or 为假时的结果
class Solution:
    """
    @param n: the integer to be reversed
    @return: the reversed integer
    """

    # time:2943 ms
    def reverseInteger(self, n):
        r = 0
        if n < 0:
            n = -n
            while n > 0:
                r = r * 10 + n % 10
                n //= 10
            return -r
        else:
            while n > 0:
                r = r * 10 + n % 10
                n //= 10
            return 0 if r >= 2 ** 32 else r

    """
    #  time:2593ms
    def reverseInteger(self, n):
        # write your code here
        if n >= 0:
            return 0 if int(str(n)[::-1])> 2**32 else return int(str(n)[::-1])  
        else:
            return int('-' + str(n)[:0:-1])
    """


s = Solution()
print(s.reverseInteger(-123))
