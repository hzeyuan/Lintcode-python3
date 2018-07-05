"""
638. Isomorphic Strings
给定两个字符串 s 和 t ，确定它们是否是同构的。
两个字符串是同构的如果 s 中的字符可以被替换得到 t。
所有出现的字符必须用另一个字符代替，同时保留字符串的顺序。 没有两个字符可以映射到同一个字符，但一个字符可以映射到自己。

样例
给出 s = "egg", t= "add", 返回 true。
给出 s = "foo", t= "bar", 返回 false。
给出 s = "paper", t= "title", 返回 true。
"""


class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if the characters in s can be replaced to get t or false
    """

    def isIsomorphic(self, s, t):
        # write your code here
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]] = 0
            else:
                dict_s[s[i]] += 1
            if t[i] not in dict_t:
                dict_t[t[i]] = 0
            else:
                dict_t[t[i]] += 1
            if dict_s[s[i]] != dict_t[t[i]]:
                return False
        return True

    """
    # time:1612ms
    def isIsomorphic(self, s, t):
        # write your code here
        dict_s = {}
        dict_t = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]] = t[i]
            else:
                if dict_s[s[i]] != t[i]:
                    return False
        for i in range(len(t)):
            if t[i] not in dict_t:
                dict_t[t[i]] = s[i]
            else:
                if dict_t[t[i]] != s[i]:
                    return False
        return True    
    """


s = Solution()

print(s.isIsomorphic('egg','add'))
