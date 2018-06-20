"""
646. 第一个独特字符位置
给出一个字符串。找到字符串中第一个不重复的字符然后返回它的下标。如果不存在这样的字符，返回 -1。

样例
给出字符串 s = "lintcode"，返回 0。
给出字符串 s = "lovelintcode"，返回 2
"""


class Solution:
    """
    @param s: a string
    @return: it's index
    """

    def firstUniqChar(self, s):
        # write your code here
        if not s:
            return -1
        haxi = {}
        for i in s:
            if i not in haxi:
                haxi[i] = 1
            else:
                haxi[i] += 1
        for i in range(len(s)):
            if haxi[s[i]] == 1:
                return i
        return -1
