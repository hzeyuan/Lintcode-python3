"""
197. 排列序号
给出一个不含重复数字的排列，求这些数字的所有排列按字典序排序后该排列的编号。其中，编号从1开始。

样例
例如，排列 [1,2,4] 是第 1 个排列
"""


class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """

    # 例如排序[1, 4, 2]。
    # 1的后面有 2! 种排列；4的后面有 1! 种排列；2的后面有 0! 种排列。
    # 1的后面有0个数比它小；4的后面有1个数比它小；2的后面有0个数比它小。
    # index=2!∗0+1!∗1+0!∗0
    # 因为是从0开始计数的，最后index还需加1
    #
    # time:1107ms
    def permutationIndex(self, A):
        # write your code here
        index = 0
        jiecheng = 1
        m = len(A) - 1
        # 计算中1到n-1的阶乘
        while m > 0:
            jiecheng *= m
            m -= 1
        # 两个循环，找出比A[i]小的数字的次数
        for i in range(len(A)):
            count = 0
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    count += 1
            index += jiecheng * count
            if i == len(A) - 1:
                jiecheng = 0
            else:
                jiecheng = jiecheng // (len(A) - 1 - i)
        return index + 1
