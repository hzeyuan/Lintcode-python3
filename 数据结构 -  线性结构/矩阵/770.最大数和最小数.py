"""
770. 最大数和最小数
给定一个矩阵，返回矩阵中的最大数和最小数

样例
给定一个矩阵:

[
 [1,2,3],
 [4,3,2],
 [6,4,4]
]
返回 [6,1]
"""


class Solution:
    """
    @param matrix: an input matrix
    @return: nums[0]: the maximum,nums[1]: the minimum
    """
    # time: 352ms
    def maxAndMin(self, matrix):
        # write your code here
        if not matrix:
            return []
        res = [-float('inf'), float('inf')]
        for i in matrix:
            maxN, minN = max(i), min(i)
            if maxN > res[0]:
                res[0] = maxN
            if minN < res[1]:
                res[1] = minN
        return res
