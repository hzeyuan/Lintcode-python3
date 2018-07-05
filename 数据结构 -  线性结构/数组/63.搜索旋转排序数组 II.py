"""
63. 搜索旋转排序数组 II
跟进“搜索旋转排序数组”，假如有重复元素又将如何？

是否会影响运行时间复杂度？

如何影响？

为何会影响？

写出一个函数判断给定的目标值是否出现在数组中。

样例
给出[3,4,4,5,7,0,1,2]和target=4，返回 true
"""


class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean
    """
    # 找到对称轴，用两次二分查找
    # time:1326 ms
    def search(self, A, target):
        # write your code here
        if not A:
            return False
        index = 0
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                index = i + 1
                break

        first_arrays = self.binary_search(A[:index], target)
        second_arrays = self.binary_search(A[index:], target)
        if first_arrays >= 0 or second_arrays >= 0:
            return True
        return False

    def binary_search(self, Arrays, target):
        left, right = 0, len(Arrays) - 1
        while left <= right:
            mid = (left + right) // 2
            if Arrays[mid] < target:
                left = mid + 1
            elif Arrays[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1


s = Solution()
print(s.search([2, 2, 2, 3, 1], 1))
