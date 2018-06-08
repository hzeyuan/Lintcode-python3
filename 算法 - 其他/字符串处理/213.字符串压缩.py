"""
213. 字符串压缩
设计一种方法，通过给重复字符计数来进行基本的字符串压缩。

例如，字符串 aabcccccaaa 可压缩为 a2b1c5a3 。而如果压缩后的字符数不小于原始的字符数，则返回原始的字符串。

可以假设字符串仅包括a-z的字母。

样例
str=aabcccccaaa 返回 a2b1c5a3
str=aabbcc 返回 aabbcc
str=aaaa 返回 a4
"""


class Solution:
    """
    @param str: a string
    @return: a compressed string
    """
    # time:704ms
    def compress(self, str):
        # write your code here
        if str is "": return str
        j = 0
        string = ''
        for i in range(1, len(str)):
            if str[i] != str[i - 1]:
                s = str[j:i]
                j = i
                length = len(s)
                string += s[0] + f'{length}'
        s = str[j:]
        string += s[0] + f'{len(s)}'
        return string if len(string)<len(str) else str



