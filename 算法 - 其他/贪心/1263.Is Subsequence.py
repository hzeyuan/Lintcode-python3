"""
1263. Is Subsequence
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of
the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of
"abcde" while "aec" is not).

样例
Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

挑战 If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T
has its subsequence. In this scenario, how would you change your code? """


class Solution:
    """
    @param s: the given string s
    @param t: the given string t
    @return: check if s is subsequence of t
    """

    # 贪心算法
    # time:1108 ms
    def isSubsequence(self, s, t):
        # Write your code here
        if not s:
            return True
        elif not t:
            return False
        j = 0
        for i in t:
            if s[j] == i:
                j += 1
            if j == len(s):
                return True
        return False


s = Solution()
print(s.isSubsequence("", "ahbgdc"))
