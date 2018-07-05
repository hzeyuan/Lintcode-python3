"""
678. Shortest Palindrome
给一个字符串 S, 你可以通过在前面添加字符将其转换为回文串.找到并返回用这种方式转换的最短回文串.

样例
给出 "aacecaaa", 返回 "aaacecaaa"
给出 "abcd", 返回 "dcbabcd"
"""


class Solution:
    """
    @param str: String
    @return: String
    """
    # O(n2)
    # time:1006ms
    def convertPalindrome(self, str):
        # Write your code here
        if not str:
            return ''
        for i in range(len(str), 0, -1):
            s = str[:i]
            if self.huiwen(s):
                return str[:i-1:-1] + str

    def huiwen(self, s):
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


s = Solution()
print(s.convertPalindrome('aacecaaa'))
