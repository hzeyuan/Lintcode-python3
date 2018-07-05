"""
664. 数 1
给以 非负 整数 num. 对所有满足 0 ≤ i ≤ num 条件的数字 i 均需要计算其二进制表示 1 的个数并以数组的形式返回

样例
给出 num = 5 你需要返回 [0,1,1,2,1,2].

挑战
时间复杂度为 O(n * sizeof(integer))的解法很容易想到, 但是你是否可以用线性的时间复杂度 O(n)/可能只遍历一遍吗, 空间复杂度应为 O(n).
你能霸气的完成这项挑战吗? 不借助任何内嵌的函数, 比如C++ 中的__builtin_popcount 亦或是任何其他语言中的方法
"""


class Solution:
    """
    @param num: a non negative integer number
    @return: an array represent the number of 1's in their binary
    """

    # time:2025ms
    def countBits(self, num):
        # write your code here
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            n = res[i >> 1]
            res[i] = n + (i & 1)
        return res


s = Solution()
print(s.countBits(10))
