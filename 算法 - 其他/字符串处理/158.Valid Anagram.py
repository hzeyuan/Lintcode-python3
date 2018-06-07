"""
158. Valid Anagram
写出一个函数 anagram(s, t) 判断两个字符串是否可以通过改变字母的顺序变成一样的字符串。

样例
给出 s = "abcd"，t="dcab"，返回 true.
给出 s = "ab", t = "ab", 返回 true.
给出 s = "ab", t = "ac", 返回 false.

挑战
O(n) time, O(1) extra space
"""


class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """

    """  
    # 一开始想到的,排序后判断相等
    # time:1812 ms
     def anagram(self, s, t):
        # write your code here
        s, t = list(s), list(t)
        s.sort()
        t.sort()
        return s == t
    """
    # 哈希表，判断两个字符串相同字母的个数是否相等
    # time:1165 ms
    def anagram(self, s, t):
        table = {i: 0 for i in range(65,123)}
        table.setdefault(32, 0)
        for i in range(len(s)):
            table[ord(s[i])] += 1
        for i in range(len(t)):
            table[ord(t[i])] -= 1
        for i in table.values():
            if i != 0:
                return False
        return True



