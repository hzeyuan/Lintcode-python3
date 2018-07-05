"""
78. 最长公共前缀
给k个字符串，求出他们的最长公共前缀(LCP)

样例
在 "ABCD" "ABEF" 和 "ACEF" 中,  LCP 为 "A"

在 "ABCDEFG", "ABCEFG", "ABCEFA" 中, LCP 为 "ABC"
"""


class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    # 两两比较
    # time:1409 ms
    def longestCommonPrefix(self, strs):
        # write your code here
        if not strs:
            return ''
        while len(strs) > 1:
            str1 = strs.pop()
            str2 = strs.pop()
            strs.append(self.CommonPrefix(str1, str2))
        return strs[0]

    def CommonPrefix(self, str1, str2):
        s = ''
        for i, j in zip(str1, str2):
            if i == j:
                s += i
            else:
                break
        return s


s = Solution()
print(s.longestCommonPrefix(["ABCD", "ABEF", "ACEF"]))
