"""
198. 排列序号II
给出一个可能包含重复数字的排列，求这些数字的所有排列按字典序排序后该排列在其中的编号。编号从1开始。

样例
给出排列[1, 4, 2, 2]，其编号为3。
"""


class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """

    def permutationIndexII(self, A):
        if A is None or len(A) == 0:
            return 0

        index, factor, multi_fact = 1, 1, 1
        counter = {}
        for i in range(len(A) - 1, -1, -1):
            if A[i] not in counter:
                    counter[A[i]] = 0
            counter[A[i]] += 1
            multi_fact *= counter[A[i]]
            rank = 0
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    rank += 1

            index += rank * factor / multi_fact
            factor *= (len(A) - i)

        return index

s = Solution()
print(s.permutationIndexII([1,3,2]))
