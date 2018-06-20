"""
627. 最长回文串
给出一个包含大小写字母的字符串。求出由这些字母构成的最长的回文串的长度是多少。

数据是大小写敏感的，也就是说，"Aa" 并不会被认为是一个回文串。

样例
给出 s = "abccccdd" 返回 7

一种可以构建出来的最长回文串方案是 "dccaccd"。
"""


class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    # time:1611ms
    def longestPalindrome(self, s):
        # write your code here
        haxi = {}
        length = len(s)
        for i in s:
            if i not in haxi:
                haxi[i] = 1
            else:
                haxi[i] += 1
        if len(haxi) == 1:
            return len(s)
        for i in haxi:
            if haxi[i] % 2 == 0:
                length -= haxi[i]
            elif haxi[i] % 2 == 1:
                length -= haxi[i] - 1
        if length == 0:
            return len(s)
        else:
            return len(s) - length + 1


s = Solution()
print(s.longestPalindrome("NTrQdQGgwtxqRTSBOitAXUkwGLgUHtQOmYMwZlUxqZysKpZxRoehgirdMUgy"))
