"""
142. O(1)时间检测2的幂次
用 O(1) 时间检测整数 n 是否是 2 的幂次。

样例
n=4，返回 true;

n=5，返回 false.

挑战
O(1) time
"""


class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    # 思路：如果一个数是2的次方数的话，那么它的二进数必然是最高位为1，其它都为0，
    # 那么如果此时我们减1的话，则最高位会降一位，其余为0的位现在都为变为1，那么我们把两数相与，就会得到0，
    # 用这个性质也能来解题
    # 3510 ms
    def checkPowerOf2(self, n):
        # write your code here
        if n == 0:
            return False
        return True if n - 1 & n == 0 else False
