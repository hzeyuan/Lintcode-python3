"""
3. 统计数字
计算数字k在0到n中的出现的次数，k可能是0~9的一个值

样例
例如n=12，k=1，在 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]，我们发现1出现了5次 (1, 10, 11, 12)
"""


class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """
    # time:1406 ms
    def digitCounts(self, k, n):
        # write your code here
        count = 0
        for i in range(n + 1):
            for j in str(i):
                if k == int(j):
                    count += 1
        return count
