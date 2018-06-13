"""
141. x的平方根
实现 int sqrt(int x) 函数，计算并返回 x 的平方根。

样例
sqrt(3) = 1

sqrt(4) = 2

sqrt(5) = 2

sqrt(10) = 3

挑战
O(log(x))
"""


class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    # time:881 ms
    def sqrt(self, x):
        # write your code here
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            square = mid ** 2
            if square == x or square < x < (mid + 1) ** 2 or square > x > (mid - 1) ** 2:
                return mid
            elif square > x:
                right = mid - 1
            else:
                left = mid + 1
            if right >= 46341:
                right = 46340


s = Solution()
print(s.sqrt(0))
