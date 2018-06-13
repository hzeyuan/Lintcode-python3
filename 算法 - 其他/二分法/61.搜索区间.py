"""
61. 搜索区间
给定一个包含 n 个整数的排序数组，找出给定目标值 target 的起始和结束位置。

如果目标值不在数组中，则返回[-1, -1]

样例
给出[5, 7, 7, 8, 8, 10]和目标值target=8,

返回[3, 4]

挑战
时间复杂度 O(log n)
"""


class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    #  time:826ms
    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1, -1]
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > A[mid]:
                left = mid + 1
            elif target < A[mid]:
                right = mid - 1
            else:
                index1, index2 = mid, mid
                while True:
                    if A[index1] == A[mid]:
                        index1 -= 1
                        if index1 < 0:
                            break
                    else:
                        break
                while True:
                    if A[index2] == A[mid]:
                        index2 += 1
                        if index2 > len(A) - 1:
                            break
                    else:
                        break
                return [index1 + 1, index2 - 1]
        return [-1,-1]


s = Solution()
print(s.searchRange([], 7))
