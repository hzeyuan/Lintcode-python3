"""
671. 循环单词
The words are same rotate words if rotate the word to the right by loop, and get another. Count how many different rotate word sets in dictionary.

E.g. picture and turepic are same rotate words.

样例
Given dict = ["picture", "turepic", "icturep", "word", "ordw", "lint"]
return 3.

"picture", "turepic", "icturep" are same ratote words.
"word", "ordw" are same too.
"lint" is the third word that different from the previous two words.
"""


class Solution:
    """
    @param: words: A list of words
    @return: Return how many different rotate words
    """
    # 将每个String的变化串加进Set集合中，进行重复判断。
    # time:514 ms
    def countRotateWords(self, words):
        count = 0
        s = set()
        for w in words:
            if w not in s:
                count += 1
                s.add(w)
                change = words[len(words) - 1:] + words[0:len(words) - 1]
                while change != w:
                    s.add(change)
                    change = self.change_word(change)
        return count

    def change_word(self, words):
        return words[len(words) - 1:] + words[0:len(words) - 1]

    """
    # 88%的时候凉了
    def countRotateWords(self, words):
        # Write your code here
        if not len(words):
            return 0
        s = [words[0]]
        for i in range(1, len(words)):
            n = 0
            for j in s:
                if self.judge_loop_words(j, words[i], 0):
                    break
                else:
                    n += 1
            if n == len(s):
                s.insert(0,words[i])
        return len(s)

    def judge_loop_words(self, words, target, numbers):
        if len(words) != len(target) or numbers == len(words):
            return False
        if words == target:
            return True
        else:
            numbers += 1
            return self.judge_loop_words(words[len(words) - 1:] + words[:len(words) - 1], target, numbers)    
    """
