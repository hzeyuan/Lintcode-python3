"""
835. Hamming Distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

样例
Input: x = 1, y = 4

Output: 2
"""


class Solution:
    """
    @param x: an integer
    @param y: an integer
    @return: return an integer, denote the Hamming Distance between two integers
    """

    # 汉明距离：汉明距离是使用在数据传输差错控制编码里面的，汉明距离是一个概念，它表示两个（相同长度）字对应位不同的数量，我们以d（x,y）表示两个字x,y之间的汉明距离。对两个字符串进行异或运算，并统计结果为1的个数，那么这个数就是汉明距离。
    # time:625 ms
    def hammingDistance(self, x, y):
        # write your code here
        xor = x ^ y
        count = 0
        while xor != 0:
            xor = xor & (xor - 1)
            count += 1
        return count
