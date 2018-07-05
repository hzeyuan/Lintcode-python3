"""
418. 整数转罗马数字
给定一个整数，将其转换成罗马数字。

返回的结果要求在1-3999的范围内。

样例
4 -> IV

12 -> XII

21 -> XXI

99 -> XCIX
"""


class Solution:
    """
    @param n: The integer
    @return: Roman representation
    """

    # time:2100ms
    def intToRoman(self, n):
        # write your code here
        digit1_to_9 = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", '']
        digit10_to_90 = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC", '']
        digit100_to_900 = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM", '']
        digit1000_to_3000 = ["M", "MM", "MMM", '']
        if n < 10:
            return digit1_to_9[n - 1]
        elif n < 100:
            n = str(n)
            return digit10_to_90[int(n[0]) - 1] + digit1_to_9[int(n[1]) - 1]
        elif n < 1000:
            n = str(n)
            return digit100_to_900[int(n[0]) - 1] + digit10_to_90[int(n[1]) - 1] + digit1_to_9[int(n[2]) - 1]
        elif n < 10000:
            n = str(n)
            return digit1000_to_3000[int(n[0]) - 1] + digit100_to_900[int(n[1]) - 1] + digit10_to_90[
                int(n[2]) - 1] + digit1_to_9[int(n[3]) - 1]


s = Solution()
print(s.intToRoman(3998))
