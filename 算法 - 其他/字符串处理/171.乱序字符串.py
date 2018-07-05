"""
171. 乱序字符串
给出一个字符串数组S，找到其中所有的乱序字符串(Anagram)。如果一个字符串是乱序字符串，那么他存在一个字母集合相同，但顺序不同的字符串也在S中。

样例
对于字符串数组 ["lint","intl","inlt","code"]

返回 ["lint","inlt","intl"]

挑战
What is Anagram?

Two strings are anagram if they can be the same after change the order of characters.
"""


class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    # time:1503ms
    def anagrams(self, strs):
        # write your code here
        dict = {}
        for word in strs:
            words = ''.join(sorted(word))
            dict[words] = [word] if words not in dict else dict[words] + [word]
        res = []
        for item in dict:
            if len(dict[item]) >= 2:
                res += dict[item]
        return res


s = Solution()
print(s.anagrams(["lint", "intl", "inlt", "code"]))
a= [1,2]
b =[3,4]
print(a+b)