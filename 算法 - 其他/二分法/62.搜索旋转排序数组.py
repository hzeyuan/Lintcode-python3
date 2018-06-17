"""
62. 搜索旋转排序数组
假设有一个排序的按未知的旋转轴旋转的数组(比如，0 1 2 4 5 6 7 可能成为4 5 6 7 0 1 2)。给定一个目标值进行搜索，如果在数组中找到目标值返回数组中的索引位置，否则返回-1。

你可以假设数组中不存在重复的元素。

样例
给出[4, 5, 1, 2, 3]和target=1，返回 2

给出[4, 5, 1, 2, 3]和target=0，返回 -1

挑战
O(logN) time
"""


class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """

    # 我的思路先遍历第一个递增的数组
    # 递增数组中，若第一个数比target大,则后面的数字肯定比target大，所以用count记录这个递增数组的长度,说明target可能数组在后半部分，然后用二分法查找。
    # 若第一个数字比target小，则找到这个值输出下标，当数组中的数字比target时，说明数字不存在输出-1
    #
    # time:1208ms
    def search(self, A, target):
        # write your code here
        if not A:
            return -1
        count = 0
        for i in range(len(A) - 1):
            if A[i] > target:
                if A[i] > A[i + 1]:
                    count = i + 1
                    break
            elif A[i] < target:
                if target == A[i]:
                    return i
                elif A[i] > target:
                    return -1
            elif target == A[i]:
                return i

        left, right = count, len(A) - 1
        while left <= right:
            mid = (left + right) // 2
            if A[mid] < target:
                left = mid + 1
            elif A[mid] > target:
                right = mid - 1
            else:
                return mid


s = Solution()
print(s.search([1001, 10001, 10007, 1, 10, 101, 201], 10001))
