"""
684. 缺少的字符串
给出两个字符串，你需要找到缺少的字符串

样例
给一个字符串 str1 = This is an example, 给出另一个字符串 str2 = is example
返回 ["This", "an"]
"""


class Solution:
    """
    @param str1: a given string
    @param str2: another given string
    @return: An array of missing string
    """
    # time:763 ms
    def missingString(self, str1, str2):
        # Write your code here
        res = []
        a = [i for i in str1.split(' ')]
        b = [i for i in str2.split(' ')]
        c = set(a) - set(b) if len(str1) >= len(str2) else set(b) - set(a)
        maxLengthString = a if len(str1) >= len(str2) else b
        for i in maxLengthString:
            if i in c:
                res.append(i)
        return res



s = Solution()
print(s.missingString('This is an example', "is example"))
