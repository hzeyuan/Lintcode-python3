"""
408. 二进制求和
给定两个二进制字符串，返回他们的和（用二进制表示）。

样例
a = 11

b = 1

返回 100
"""


class Solution:
    """
    @param a: a number
    @param b: a number
    @return: the result
    """
    # 直接用内置函数
    # time:1323ms
    def addBinary(self, a, b):
        # write your code here
        return '{:b}'.format(int(a, 2) + int(b, 2))

    """
    # time:1337ms
    def addBinary(self, a, b):
       r = str(int(a) + int(b))
       n = 0
       res = ''
       for i in range(len(r) - 1, 0, -1):
           if int(r[i])+n ==2:
               res += '0'
               n = 1
           elif int(r[i])+n == 3:
               res += '1'
               n = 1
           else:
               res += str(int(r[i])+n)
               n = 0
       if int(r[0])+n ==2:
           res += '01'
       elif int(r[0])+n == 3:
           res +='11'
       else:
          res += str(int(r[0])+n)
       return res[::-1]
    """



s = Solution()
print(s.addBinary('110', '1'))
