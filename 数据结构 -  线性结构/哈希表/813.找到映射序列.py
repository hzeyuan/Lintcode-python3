"""
813. 找到映射序列
给出了两个A和B的列表，从A映射到B，B是由A的一种回文构词法构成通过随机化A中元素的顺序来实现的。
我们想要找到一个指数映射P，从A到B，映射P[i] = j表示A出现在B中的第i个元素。
这些列表A和B可能包含重复。如果有多个答案，输出任何一个。

样例
给定A =[12, 28, 46, 32, 50]和B =[50, 12, 32, 46, 28]，返回[1, 4, 3, 2, 0]。

解释:
P[0] = 1，因为A的第0个元素出现在B[1]， P[1] = 4，因为A的第一个元素出现在B[4]，以此类推。
"""


class Solution:
    """
    @param A: lists A
    @param B: lists B
    @return: the index mapping
    """
    # time:705 ms
    def anagramMappings(self, A, B):
        # Write your code here
        haxi = {}
        res = []
        for i in range(len(B)):
            if B[i] not in haxi:
                haxi[B[i]] = i
        for i in range(len(A)):
            res.append(haxi[A[i]])
        return res


s = Solution()
print(s.anagramMappings([12, 28, 46, 32, 50], [50, 12, 32, 46, 28]))
