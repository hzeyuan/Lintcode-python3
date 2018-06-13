"""
28. 搜索二维矩阵
写出一个高效的算法来搜索 m × n矩阵中的值。

这个矩阵具有以下特性：

每行中的整数从左到右是排序的。
每行的第一个数大于上一行的最后一个整数。
样例
考虑下列矩阵：

[
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
给出 target = 3，返回 true

挑战
O(log(n) + log(m)) 时间复杂度
"""


class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    """
    # f方法1：这个代码少点
    # time: 1256 ms
    def searchMatrix(self, matrix, target):
        # write your code here
        from itertools import chain
        if target in list(chain(*matrix)):
            return True
        else:
            return False
    """

    # 在上面的基础上，优化下，二分查找：
    # time:1172ms
    def searchMatrix(self, matrix, target):
        # write your code here
        from itertools import chain
        matrix = list(chain(*matrix))
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[mid]:
                left = (left + right) // 2 + 1
            elif target < matrix[mid]:
                right = (left + right) // 2 - 1
            else:
                return True
        return False


s = Solution()
print(s.searchMatrix([
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
], 10))
