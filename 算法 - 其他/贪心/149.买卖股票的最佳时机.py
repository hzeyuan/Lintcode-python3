"""
149. 买卖股票的最佳时机
假设有一个数组，它的第i个元素是一支给定的股票在第i天的价格。如果你最多只允许完成一次交易(例如,一次买卖股票),设计一个算法来找出最大利润。

样例
给出一个数组样例 [3,2,3,1,2], 返回 1
"""


class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """

    def maxProfit(self, prices):
        # write your code here
        count = 0
        low = float('inf')
        for i in range(len(prices)):
            if prices[i] - low > count:
                count = prices[i] - low
            if prices[i] < low:
                low = prices[i]
        return count


s = Solution()
print(s.maxProfit([1, 50, 2, 72, 1, 5, 61]))
