"""
419. 罗马数字转整数
给定一个罗马数字，将其转换成整数。

返回的结果要求在1到3999的范围内。

样例
IV -> 4

XII -> 12

XXI -> 21

XCIX -> 99
"""


class Solution:
    """
    @param s: Roman representation
    @return: an integer
    """
    # time:1424 ms
    def romanToInt(self, s):
        # write your code here
        digit1_to_3999 = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
                          "XX": 20, "XXX": 30, "XL": 40, "L": 50, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90, "C": 100,
                          "CC": 200, "CCC": 300, "CD": 400, "D": 500, "DC": 600, "DCC": 700, "DCCC": 800,
                          "CM": 900, "M": 1000, "MM": 2000, "MMM": 3000}
        digit = 0
        ptr = 0
        while ptr < len(s):
            string = s[ptr]
            while True:
                if string in digit1_to_3999:
                    number = digit1_to_3999[string]
                    ptr += 1
                    if ptr >= len(s):
                        break
                    string += s[ptr]
                else:
                    break
            digit += number
        return digit


s = Solution()
print(s.romanToInt("MMCCCXCIX"))
