"""
172. 删除元素
给定一个数组和一个值，在原地删除与值相同的数字，返回新数组的长度。

元素的顺序可以改变，并且对新的数组不会有影响。

样例
给出一个数组 [0,4,4,0,0,2,4,4]，和值 4

返回 4 并且4个元素的新数组为[0,0,0,2]
"""


class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """

    # 把等于elem的数字放到后面去
    # time:1409ms
    def removeElement(self, A, elem):
        # write your code here
        j = len(A) - 1
        for i in range(len(A) - 1, -1, -1):
            if A[i] == elem:
                A[i], A[j] = A[j], A[i]
                j -= 1
        return j + 1


s = Solution()
print(s.removeElement([0, 4, 4, 0, 4, 4, 4, 0, 2], 4))
