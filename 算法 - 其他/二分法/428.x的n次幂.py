"""
428. x的n次幂
实现 pow(x,n)

样例
Pow(2.1, 3) = 9.261
Pow(0, 1) = 0
Pow(1, 0) = 1
挑战
O(logn) time
"""


class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """
    # time:2215ms
    def myPow(self, x, n):
        # write your code here
        y = 1
        k = x
        while n:
            if n % 2 == 1:
                y = y * k

            k = k * k
            n //= 2

        return y


s = Solution()
print(s.myPow(2.0, 20))
