"""
792. Kth Prime Number
给出质数n，输出它是第几个质数。

样例
给出 n = 3，返回 2。

解释：
[2,3,5]，3是第2个质数。
给出 n = 11，返回 5。

解释：
[2,3,5,7,11]，11是第五个质数。
"""


class Solution:
    """
    @param n: the number
    @return: the rank of the number
    """

    # time:1007ms
    def kthPrime(self, n):
        # write your code here
        res = []
        for i in range(2, n + 1):
            if self.zhishu(i):
                res.append(i)
        return res

    # 6素数法
    def zhishu(self, n):
        import math
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        k = int(math.sqrt(n) + 1)
        for i in range(5, k, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True


s = Solution()
print(s.kthPrime(11))
