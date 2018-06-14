"""
697. Sum of Square Numbers
给一个整数 c, 你需要判断是否存在两个整数 a 和 b 使得 a^2 + b^2 = c.

样例
给出 n = 5
返回 true // 1 * 1 + 2 * 2 = 5
给出 n = -5
返回 false
"""


class Solution:
    """
    @param num: the given number
    @return: whether whether there're two integers
    """
    # time:1059 ms
    def checkSumOfSquareNumbers(self, num):
        # write your code here
        if num < 0:
            return False
        else:
            import math
            left, right = 0, int(math.sqrt(num))
            while left <= right:
                a_b_num = left ** 2 + right ** 2
                if a_b_num < num:
                    left += 1
                elif a_b_num > num:
                    right -= 1
                else:
                    return True
        return False
