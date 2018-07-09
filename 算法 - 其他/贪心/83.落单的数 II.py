"""
83. 落单的数 II
给出3*n + 1 个的数字，除其中一个数字之外其他每个数字均出现三次，找到这个数字。

样例
给出 [1,1,2,3,3,3,2,2,4,1] ，返回 4

挑战
一次遍历，常数级的额外空间复杂度
"""


class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    # time:2078ms
    def singleNumberII(self, A):
        # write your code here
        r = [0] * 32
        for x in A:
            for i in range(len(r)):
                if (1 << i) & x > 0:
                    r[i] += 1
                if 1 << i > x:
                    break
        res = 0
        for i in range(len(r)):
            t = r[i] % 3
            if t == 1:
                res += 1 << i
        return res


s = Solution()
print(s.singleNumberII([1, 1, 2, 3, 3, 3, 2, 2, 4, 1]))
