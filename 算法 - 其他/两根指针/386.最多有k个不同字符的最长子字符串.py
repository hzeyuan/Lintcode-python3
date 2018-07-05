"""
386. 最多有k个不同字符的最长子字符串
给定一个字符串，找到最多有k个不同字符的最长子字符串。

样例
例如，给定 s = "eceba" , k = 3,

T 是 "eceb"，长度为 4.

挑战
O(n), n 是所给字符串的长度
"""


class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    # time:2431ms
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if not s or k == 0:
            return 0
        elif len(s) < k:
            return len(s)
        number = 0
        j = 0
        haxi = {}
        for i in range(len(s) - k + 1):
            while j < len(s):
                if len(haxi) >= k and s[j] not in haxi:
                    break
                if s[j] not in haxi:
                    haxi[s[j]] = 1
                else:
                    haxi[s[j]] += 1
                j += 1
            if j == len(s) and j - i > number:
                return j - i
            st = max(len(s[i:j]), number)
            haxi[s[i]] -= 1
            if haxi[s[i]] == 0:
                haxi.pop(s[i])
        return number


s = Solution()
print(s.lengthOfLongestSubstringKDistinct('eceba'))


