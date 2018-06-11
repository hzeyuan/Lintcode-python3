"""

927. 翻转字符串II
给定输入的字符数组，逐词翻转数组。单词被定义为不包含空格的字符串.
输入字符数组不包含前导或尾部空格，单词总是用单个空格分隔。

样例
给定 s = "the sky is blue",
翻转之后 : "blue is sky the"

挑战
你能在不分配额外空间的情况下原地解决这个问题吗？
"""


class Solution:
    """
    @param str: a string
    @return: return a string
    """
    # time:1009 ms
    def reverseWords(self, str):
        # write your code here
        return ' '.join(str.split(' ')[::-1])
s =Solution()
print(s.reverseWords('the sky is blue'))
