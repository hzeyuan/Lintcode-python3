"""
744. 前K个偶数长度的回文数和
给一整数 k, 得出前 k 个偶数长度的回文数和. 这里的偶数长度是指一个数字的位数为偶数.

样例
给出 k = 3, 返回 66 // 11 + 22 + 33 = 66 (前三个偶数长度的回文数和)
给出 k = 10, 返回 1496 // 11 + 22 + 33 + 44 + 55 + 66 + 77 + 88 + 99 + 1001 = 1496
"""


class Solution:
    """
    @param k: Write your code here
    @return: the sum of first k even-length palindrome numbers
    """

    # time:762 ms
    def sumKEven(self, k):
        n = 0
        for i in range(1, k + 1):
            s = str(i) + str(i)[::-1]
            n += int(s)
        return n


s = Solution()
print(s.sumKEven(10))
