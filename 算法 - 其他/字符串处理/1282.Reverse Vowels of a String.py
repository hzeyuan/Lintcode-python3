"""
1282. Reverse Vowels of a String
Write a function that takes a string as input and reverse only the vowels of a string.

样例
Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "lintcode", return "lentcodi".
"""


class Solution:
    """
    @param s: a string
    @return: reverse only the vowels of a string
    """
    # 从左右两边交换元音字母，用一个字符串从左到右加到结束
    # time:630ms
    def reverseVowels(self, s):
        # write your code here
        s = list(s)
        res = ''
        yuanyin = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left, right = 0, len(s) - 1
        while left < len(s):
            while left < len(s)-1 and s[left] not in yuanyin:
                res += s[left]
                left += 1
            while s[right] not in yuanyin and left <= right:
                right -= 1
            if left < right:
                s[left], s[right] = s[right], s[left]
            res += s[left]
            left += 1
            right -= 1
        return res


s = Solution()
print(s.reverseVowels("lintcode"))
