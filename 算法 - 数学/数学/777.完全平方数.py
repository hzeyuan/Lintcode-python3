"""
777. 完全平方数
给出一个正整数 'num,写一个函数，要求当这个当num为完全平方数时函数返回True，否则返回False

样例
举例：
给出num=16
返回 True
"""


class Solution:
    """
    @param num: a positive integer
    @return: if num is a perfect square else False
    """
    # time: 753ms
    def isPerfectSquare(self, num):
        # write your code here
        if num ==1:
            return True
        for i in range(1, num // 2):
            if i * i == num:
                return True
            if i * i > num:
                return False


s = Solution()
print(s.isPerfectSquare(1))
