"""
487. 姓名去重
给一串名字，将他们去重之后返回。两个名字重复是说在忽略大小写的情况下是一样的。

样例
给出：

[
  "James",
  "james",
  "Bill Gates",
  "bill Gates",
  "Hello World",
  "HELLO WORLD",
  "Helloworld"
]
返回：

[
  "james",
  "bill gates",
  "hello world",
  "helloworld"
]
返回名字必须都是小写字母。
"""


class Solution:
    """
    @param names: a string array
    @return: a string array
    """
    # time:1057 ms
    def nameDeduplication(self, names):
        # write your code here
        haxi = {}
        res = []
        for i in names:
            lower_letter = i.lower()
            if lower_letter not in haxi:
                haxi[lower_letter] = 1
                res.append(lower_letter)
        return res


s = Solution()
print(s.nameDeduplication([
    "James",
    "james",
    "Bill Gates",
    "bill Gates",
    "Hello World",
    "HELLO WORLD",
    "Helloworld"
]))

