"""
157. 判断字符串是否没有重复字符
实现一个算法确定字符串中的字符是否均唯一出现

样例
给出"abc"，返回 true

给出"aab"，返回 false

挑战
如果不使用额外的存储空间，你的算法该如何改变？
"""


class Solution:
    """
    @param: str: A string
    @return: a boolean
    """

    # time:843ms
    def isUnique(self, str):
        for i in range(len(str)):
            if str[i] in str[i + 1:]:
                return False
        return True
