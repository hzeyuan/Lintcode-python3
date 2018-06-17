"""
764. 计算圆周长和面积
给定半径r，返回圆的周长nums[0]和面积nums[1].结果保留了两位小数.

样例
给定 r = 2
return [12.56, 12.56]
"""


class Solution:
    """
    @param r: a Integer represent radius
    @return: the circle's circumference nums[0] and area nums[1]
    """
    # time:353 ms
    def calculate(self, r):
        # write your code here
        import math
        return [r * 2 * 3.14, r * r * 3.14]
s =Solution()
print(s.calculate(2))