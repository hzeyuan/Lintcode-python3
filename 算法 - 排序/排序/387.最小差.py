"""
387. 最小差
给定两个整数数组（第一个是数组 A，第二个是数组 B），在数组 A 中取 A[i]，数组 B 中取 B[j]，A[i] 和 B[j]两者的差越小越好(|A[i] - B[j]|)。返回最小差。

样例
给定数组 A = [3,4,6,7]， B = [2,3,8,9]，返回 0。

挑战
时间复杂度 O(n log n)
"""


class Solution:
    """
    @param A: An integer array
    @param B: An integer array
    @return: Their smallest difference.
    """

    # 排序两个数组，用两个指针指向初始位置
    # if A[i]>B[j] j++
    # if A[i]<B[j] i++
    # time:2270ms
    def smallestDifference(self, A, B):
        # write your code here
        if A is None or B is None:
            return 0
        MIN = abs(A[0] - B[0])
        i, j = 0, 0
        A.sort()
        B.sort()
        while i < len(A) and j < len(B):
            MIN = min(MIN, abs(A[i] - B[j]))
            if MIN == 0:
                return MIN
            elif A[i] > B[j]:
                j += 1
            else:
                i += 1
        return MIN

    """
    # 遍历另一个数组，
    # 在一个排序好的数组中二分查找
    # 速度好慢
    # time:4687ms
    def smallestDifference(self, A, B):
        # write your code here
        B.sort()

        res = float('inf')
        if len(A) == 0 or len(B) == 0:
            return 0
        for i in A:
            left, right = 0, len(B) - 1
            while left <= right:
                mid = (left + right) // 2
                if B[mid] == i:
                    return 0
                elif B[mid] < i:
                    left = mid + 1
                else:
                    right = mid - 1
            res = min(res, abs(i - B[mid]))
            if mid > 0:
                res = min(res, abs(i - B[mid - 1]))
            elif mid < len(B) - 1:
                res = min(res, abs(i - B[mid + 1]))
        return res
    """
