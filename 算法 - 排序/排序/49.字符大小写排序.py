"""
给定一个只包含字母的字符串，按照先小写字母后大写字母的顺序进行排序。

样例
给出"abAcD"，一个可能的答案为"acbAD"

挑战
在原地扫描一遍完成
"""


class Solution:
    """
    # 使用内置函数
    # time:1611ms
    def sortLetters(self, chars):
        # write your code here
        chars.sort(key=lambda x: x.isupper())
    """
    # 快排
    # time:1610ms
    def sortLetters(self, chars):
        # write your code here
        left, right = 0, len(chars) - 1
        while left <= right:
            while left <= right and chars[left].islower():
                left += 1
            while left <= right and chars[right].isupper():
                right -= 1
            if left <= right:
                chars[left], chars[right] = chars[right], chars[left]


s = Solution()
chars = ['a', 'b', 'A', 'c', 'D']
s.sortLetters(chars)
print(chars)