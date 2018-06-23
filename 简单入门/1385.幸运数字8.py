"""
1385. 幸运数字8
8是小九的幸运数字，小九想知道在1~n的数中有多少个数字含有8。

样例
给出 n = 20， 返回2。

解释：
只有8,18 含有8。
给出 n = 100， 返回19。
"""


class Solution:
    """
    @param n: count lucky numbers from 1 ~ n
    @return: the numbers of lucky number
    """
    # time:2038 ms
    def luckyNumber(self, n):
        # Write your code here
        count = 0
        for i in range(n):
            if '8' in str(i):
                count += 1
        return count
