"""
828. 字模式
给定一个模式和一个字符串str，查找str是否遵循相同的模式。
这里遵循的意思是一个完整的匹配，在一个字母的模式和一个非空的单词str之间有一个双向连接的模式对应。

样例
给定模式= "abba"， str = "dog cat cat dog"，返回true。给定模式= "abba"， str = "dog cat cat fish"，返回false。
给定模式= "aaaa"， str = "dog cat cat dog"，返回false。给定模式= "abba"， str = "dog dog dog dog"，返回false。
"""


class Solution:
    """
    @param pattern: a string, denote pattern string
    @param str: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    # time:906 ms
    def wordPattern(self, pattern, str):
        # write your code here
        haxi = {}
        string = ''
        for i in range(len(pattern)):
            if pattern[i] in haxi:
                haxi[pattern[i]].append(i)
            else:
                haxi[pattern[i]] = [i]
        s = str.split(' ')
        for i in haxi:
            if s[haxi[i][0]] == string:
                return False
            else:
                string = s[haxi[i][0]]
            for j in range(1, len(haxi[i])):
                if s[haxi[i][j]] == s[haxi[i][j - 1]]:
                    continue
                else:
                    return False
        return True


s = Solution()
print(s.wordPattern('abba', "dog cat cat dog"))
