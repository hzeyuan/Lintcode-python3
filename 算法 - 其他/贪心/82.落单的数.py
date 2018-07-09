"""
82. 落单的数
给出2*n + 1 个的数字，除其中一个数字之外其他每个数字均出现两次，找到这个数字。



样例
给出 [1,2,2,1,3,4,3]，返回 4

挑战
一次遍历，常数级的额外空间复杂度
"""


class Solution:
    """
    @param A: An integer array
    @return: An integer
    """

    # 定义： 同0异1； （更好的定义）不进位的二进制加法
    # 有结合律 (a ^ b) ^ c = a ^ (b ^ c)
    # 有交换律 a ^ b = b ^ a
    # a ^ a =0 抵消
    # a ^ 0 = a
    # a ^ b = c => a ^ c = b; b ^ c = a
    # 相同的都会被抵消掉成0，最后就只剩下0和那个只出现一次的数字
    # time:590ms
    def singleNumber(self, A):
        # write your code here
        ans = 0
        for x in A:
            ans = ans ^ x
        return ans


s = Solution()
print(s.singleNumber([2, 3, 2, 3, 1]))
