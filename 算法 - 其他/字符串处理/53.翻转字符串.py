"""
53. 翻转字符串
给定一个字符串，逐个翻转字符串中的每个单词
"""
class Solution:
    """
    @param: s: A string
    @return: A string
    """
    # time: 1208 ms
    def reverseWords(self, s):
        # write your code here
        res = ''
        for i in s.strip(' ').split(' ')[::-1]:
            res += i+' '

        return res.strip(' ')