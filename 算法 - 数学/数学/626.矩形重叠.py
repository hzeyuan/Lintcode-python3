"""
626. 矩形重叠
给定两个矩形，判断这两个矩形是否有重叠。

样例
给定 l1 = [0, 8], r1 = [8, 0], l2 = [6, 6], r2 = [10, 0], 返回 true

给定 l1 = [0, 8], r1 = [8, 0], l2 = [9, 6], r2 = [10, 0], 返回 false
"""


# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    """
    @param l1: top-left coordinate of first rectangle
    @param r1: bottom-right coordinate of first rectangle
    @param l2: top-left coordinate of second rectangle
    @param r2: bottom-right coordinate of second rectangle
    @return: true if they are overlap or false
    """

    def doOverlap(self, l1, r1, l2, r2):
        # write your code here
        if r2.x > l2.x > r1.x or r1.x > l1.x > r2.x:
            return False
        elif l2.y > r2.y > l1.y or l1.y > r1.y > l2.y:
            return False
        return True
