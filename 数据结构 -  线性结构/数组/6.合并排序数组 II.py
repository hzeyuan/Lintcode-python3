"""
6. 合并排序数组 II
合并两个排序的整数数组A和B变成一个新的数组。

样例
给出A=[1,2,3,4]，B=[2,4,5,6]，返回 [1,2,2,3,4,4,5,6]

挑战
你能否优化你的算法，如果其中一个数组很大而另一个数组很小
"""


class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """

    # time:980 ms
    def mergeSortedArray(self, A, B):
        # write your code here
        A.append(99999)
        B.append(99999)
        left, right = 0, 0
        newlist = []
        while True:
            if A[left] <= B[right]:
                newlist.append(A[left])
                left += 1
            else:
                newlist.append(B[right])
                right += 1
            if left + 1 == len(A):
                return newlist + B[right:-1]
            elif right + 1 == len(B):
                return newlist + A[left:-1]
