"""
211. 字符串置换
给定两个字符串，请设计一个方法来判定其中一个字符串是否为另一个字符串的置换。

置换的意思是，通过改变顺序可以使得两个字符串相等。

样例
"abc" 为 "cba" 的置换。

"aabc" 不是 "abcc" 的置换。
"""


class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """
    # 跟 158题是一样的
    # time:843 ms
    def Permutation(self, A, B):
        # write your code here
        table = {i: 0 for i in range(0, 123)}
        for i in range(len(A)):
            table[ord(A[i])] += 1
        for i in range(len(B)):
            table[ord(B[i])] -= 1
        for i in table.values():
            if i != 0:
                return False
        return True
