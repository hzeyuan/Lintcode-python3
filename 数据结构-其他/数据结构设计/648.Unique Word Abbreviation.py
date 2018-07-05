"""
648. Unique Word Abbreviation
一个单词的缩写根据以下的形式。下面是一些缩写的例子

a) it                      --> it    (没有缩写)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
假设你有一个字典和给你一个单词，判断这个单词的缩写在字典中是否是唯一的。当字典中的其他单词的缩写均与它不同的时候， 这个单词的缩写是唯一的.

样例
给出字典 dictionary = [ "deer", "door", "cake", "card" ]
isUnique("dear") // 返回 false
isUnique("cart") // 返回 true
isUnique("cane") // 返回 false
isUnique("make") // 返回 true
"""


class ValidWordAbbr:
    """
    @param: dictionary: a list of words
    """

    def __init__(self, dictionary):
        # do intialization if necessary
        self.d = {}
        for i in dictionary:
            if i not in self.d:
                self.d[i[0] + str(len(i) - 2) + i[-1]] = [i]
            else:
                self.d[i[0] + str(len(i) - 2) + i[-1]].append(i)

    """
    @param: word: a string
    @return: true if its abbreviation is unique or false
    """

    def isUnique(self, word):
        # write your code here
        w = word[0] + str(len(word) - 2) + word[-1]
        if w not in self.d:
            return True
        else:
            return self.d[w].count(word) == len(self.d[w])


# Your ValidWordAbbr object will be instantiated and called as such:
obj = ValidWordAbbr(["deer"])
param = obj.isUnique('dear')
print(param)
