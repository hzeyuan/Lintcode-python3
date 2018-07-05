"""
891. Valid Palindrome II
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

样例
Given s = "aba" return true
Given s = "abca" return true // delete c
"""


class Solution:
    """
    @param s: a string
    @return: nothing
    """
    # time:1056ms
    def validPalindrome(self, s):
        # Write your code here
        if not s:
            return False
        left, right = 0, len(s) - 1
        count = 0
        while left <= right:
            if s[left] != s[right]:
                count += 1
                if s[left + 1] == s[right]:
                    left += 1
                elif s[right - 1] == s[left]:
                    right -= 1
                else:
                    return False
            if count >= 2:
                return False
            left += 1
            right -= 1
        return True




s = Solution()
print(s.validPalindrome('abcsa'))
