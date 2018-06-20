"""
845. Greatest Common Divisor
Given two numbers, number a and number b. Find the greatest common divisor of the given two numbers.

样例
Given a = 10, b = 15, return 5.
Given a = 15, b = 30, return 15.
"""


class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """
    # time:1258 ms
    def gcd(self, a, b):
        # write your code here
        if a == 0 or b == 0:
            return 0
        max_n = 0
        res = []
        for i in range(1, a + 1):
            if a % i == 0:
                res.append(i)
        for i in res:
            if b % i == 0 and i > max_n:
                max_n = i
        return max_n


s = Solution()
print(s.gcd(30, 15))
