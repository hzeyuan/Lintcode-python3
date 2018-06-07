"""
209. First Unique Character in a String
给出一个字符串，找出第一个只出现一次的字符。

样例
对于 "abaccdeff", 'b'为第一个只出现一次的字符.
"""


class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    # 用哈希表建立每个字符和其出现次数的映射，然后按顺序遍历字符串，找到第一个出现次数为1的字符
    # time:742ms
    def firstUniqChar(self, str):
        # Write your code here
        n = {x: 0 for x in str}
        for i in str:
            n[i] += 1
        for i in n.keys():
            if n[i] == 1:
                return i


