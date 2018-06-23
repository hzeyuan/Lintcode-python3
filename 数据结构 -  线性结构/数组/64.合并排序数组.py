"""
64. 合并排序数组
合并两个排序的整数数组A和B变成一个新的数组。

样例
给出 A = [1, 2, 3, empty, empty], B = [4, 5]

合并之后 A 将变成 [1,2,3,4,5]
"""


class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    # time:942 ms
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        for i in range(len(B)):
            A[i+m] = B[i]
        A.sort()
        return A


s = Solution()
print(s.mergeSortedArray([1, 2, 3, 0, 0], 3, [4, 5], 2))
a = reversed('123')