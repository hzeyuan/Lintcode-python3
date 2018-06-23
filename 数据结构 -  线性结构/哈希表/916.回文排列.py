"""
916. 回文排列
给定一个字符串，判断字符串是否存在一个排列是回文排列。

样例
给定s = "code", 返回 False.
给定s = "aab", 返回 True.
给定s = "carerac", 返回 True.
"""


class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    # time: 965ms
    def canPermutePalindrome(self, s):
        # write your code here
        haxi = {}
        for i in s:
            if i in haxi:
                haxi[i] += 1
            else:
                haxi[i] = 1
        if len(haxi) ==1:
            return True
        count = 0
        for i in haxi:
            if haxi[i] % 2 == 1:
                count += 1
            if count > 1:
                return False
        return True


s =Solution()
print(s.canPermutePalindrome('aaaaa'))
