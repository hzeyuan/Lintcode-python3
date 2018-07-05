"""
644. Strobogrammatic Number
一个镜像数字是指一个数字旋转180度以后和原来一样(倒着看)。
写下一个函数来判断是否这个数字是镜像的。数字用字符串来表示。

样例
例如，数字"69"，"88"，和"818"都是镜像数字。
给出数字 num = "69"
返回 true
给出数字 num = "68"
返回 false
"""


class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """

    def isStrobogrammatic(self, num):
        # write your code here
        biao = {'0': '0', '1': '1', '6': '9', '9': '6', '8': '8'}
        for i in range(len(num) // 2+1):
            if num[i] not in biao or num[len(num) - 1 - i] not in biao or num[i] != biao[num[len(num) - 1 - i]]:
                return False
        return True


s = Solution()
print(s.isStrobogrammatic('69'))


