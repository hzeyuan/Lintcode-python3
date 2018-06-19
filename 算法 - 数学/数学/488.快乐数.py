"""
488. 快乐数
写一个算法来判断一个数是不是"快乐数"。

一个数是不是快乐是这么定义的：对于一个正整数，每一次将该数替换为他每个位置上的数字的平方和，然后重复这个过程直到这个数变为1，或是无限循环但始终变不到1。如果可以变为1，那么这个数就是快乐数。

样例
19 就是一个快乐数。

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""


class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """
    # 用一个集合来保存出现过的数字，来确定是否进去死循环
    # time:1913 ms
    def isHappy(self, n):
        # write your code here
        haxi = {}
        count = 0
        while count >= 0:
            count = 0
            for i in str(n):
                count += int(i) * int(i)
            n = count
            if count in haxi:
                return False
            else:
                haxi[count] = 1
            if count == 1:
                return True
s = Solution()
print(s.isHappy(19))