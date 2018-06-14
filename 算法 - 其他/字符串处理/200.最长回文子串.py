"""
200. 最长回文子串
给出一个字符串（假设长度最长为1000），求出它的最长回文子串，你可以假定只有一个满足条件的最长回文串。

样例
给出字符串 "abcdzdcab"，它的最长回文子串为 "cdzdc"。

挑战
O(n2) 时间复杂度的算法是可以接受的，如果你能用 O(n) 的算法那自然更好。
"""


class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """
    # (n^2)
    # time: 4464ms
    def longestPalindrome(self, s):
        # write your code here
        max_huiwen = ''
        if not s:
            return max_huiwen
        longest = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.huiwen(s, i, j):
                    if longest < j - i + 1:
                        longest = j - i + 1
                        max_huiwen = s[i:j + 1]
            if longest == len(s) - i:
                return max_huiwen
        return max_huiwen

    def huiwen(self, s, i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True



