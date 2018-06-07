"""
133. Longest Word
给一个词典，找出其中所有最长的单词。

样例
在词典

{
  "dog",
  "google",
  "facebook",
  "internationalization",
  "blabla"
}
中, 最长的单词集合为 ["internationalization"]

在词典
{
  "like",
  "love",
  "hate",
  "yes"
}
中，最长的单词集合为 ["like", "love", "hate"]

挑战
遍历两次的办法很容易想到，如果只遍历一次你有没有什么好办法？
"""


class Solution:
    """
    @param: dictionary: an array of strings
    @return: an arraylist of strings
    """
    # time:897ms
    def longestWords(self, dictionary):
        length = -1
        res = []
        for i in dictionary:
            if len(i) > length:
                length = len(i)
                res.clear()
                res.append(i)
            elif len(i) == length:
                res.append(i)
        return res

    # time:1010 ms
    """
    def longestWords(self, dictionary):
        max_length = -1
        l = []
        for i in dictionary:
            if len(i) > max_length:
                max_length = len(i)
        for i in dictionary:
            if len(i) == max_length:
                l.append(i)
        return l
    """

    """
    # time:1057ms
    def longestWords(self, dictionary):
        # write your code here
        res = {len(i): [] for i in dictionary}
        _ = {len(i): res[len(i)].append(i) for i in dictionary}
        return res[max(res.keys())]
    """


s = Solution()
print(s.longestWords(['a', 'ab', 'abc', 'abcde', 'bcd','edcba']))
