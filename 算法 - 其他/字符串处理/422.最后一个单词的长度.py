"""
422. 最后一个单词的长度
给定一个字符串， 包含大小写字母、空格' '，请返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

样例
给定 s = "Hello World"，返回 5。
"""


class Solution:
    """
    @param s: A string
    @return: the length of last word
    """

    # 使用内置函数
    # 1972 ms
    def lengthOfLastWord(self, s):
        # write your code here
        if s.strip() == "": return 0
        return len(s.strip().split(' ')[-1])
