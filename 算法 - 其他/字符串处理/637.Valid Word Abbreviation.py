"""
637. Valid Word Abbreviation
给定一个非空字符串 word 和缩写 abbr，返回字符串是否可以和给定的缩写匹配。
比如一个 “word” 的字符串仅包含以下有效缩写：

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
样例
样例 1:

给出 s = "internationalization", abbr = "i12iz4n":
返回 true。
样例 2:

给出 s = "apple", abbr = "a2e":
返回 false。
"""


class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    # time:1283 ms
    def validWordAbbreviation(self, word, abbr):
        # write your code here
        index, word_index = 0, 0
        while index < len(abbr):
            if abbr[index].isalpha() and abbr[index] == word[word_index]:
                index += 1
                word_index += 1
            elif abbr[index].isdigit():
                num = index
                while index < len(abbr) and abbr[index].isdigit():
                    index += 1
                word_index += int(abbr[num:index])
                if word_index > len(word) or int(abbr[num:index]) < 10*10**(len(abbr[num:index])-2):
                    return False
            elif abbr[index] != word[word_index]:
                return False
        return True


s = Solution()
print(s.validWordAbbreviation("internationalization", 'i12iz4n'))
