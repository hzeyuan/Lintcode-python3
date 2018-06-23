"""
768. 杨辉三角
给一整数 n, 返回杨辉三角的前 n 行

样例
给出 n = 4
返回
[
 [1]
 [1,1]
 [1,2,1]
 [1,3,3,1]
]
"""


class Solution:
    """
    @param n: a Integer
    @return: the first n-line Yang Hui's triangle
    """

    # time:965 ms
    def calcYangHuisTriangle(self, n):
        # write your code here
        if n == 0:
            return []
        res = [[1]]
        b = []
        while n > 1:
            b = [1] + [b[i] + b[i + 1] for i in range(len(b) - 1)] + [1]
            res.append(b)
            n -= 1
        return res


s = Solution()
print(s.calcYangHuisTriangle(10))
