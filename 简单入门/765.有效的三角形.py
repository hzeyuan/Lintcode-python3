"""
765. 有效的三角形
给出三个整数 a, b, c, 如果它们可以构成三角形,返回 true.

样例
给定 a = 2, b = 3, c = 4
返回 true
给定 a = 1, b = 2, c = 3
返回 false
"""


class Solution:
    """
    @param a: a integer represent the length of one edge
    @param b: a integer represent the length of one edge
    @param c: a integer represent the length of one edge
    @return: whether three edges can form a triangle
    """
    # time:403 ms
    def isValidTriangle(self, a, b, c):
        # write your code here
        return True if a + b > c and a + c > b and b + c > a else False
