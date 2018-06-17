"""
761. 最小子集
给一 非负 整数数组. 取数组中的一部分元素, 使得它们的和大于数组中其余元素的和, 求出满足条件的元素数量最小值.

样例
给出 nums = [3, 1, 7, 1], 返回 1
给出 nums = [2, 1, 2], 返回 2
"""


class Solution:
    """
    @param arr:  an array of non-negative integers
    @return: minimum number of elements
    """

    # time:201ms
    def minElements(self, arr):
        # write your code here
        max_arr = sum(arr)
        arr.sort(reverse=True)
        count = 1
        ans = 0
        for i in arr:
            ans += i
            if ans < max_arr - ans:
                count += 1
            else:
                return count


import math

print(math.pow(1.1, 3))

s = Solution()
print(s.minElements([2, 1, 2]))
