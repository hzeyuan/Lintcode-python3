"""
184. 最大数
给出一组非负整数，重新排列他们的顺序把他们组成一个最大的整数。

样例
给出 [1, 20, 23, 4, 8]，返回组合最大的整数应为8423201。

挑战
在 O(nlogn) 的时间复杂度内完成
"""


# 按照左边第一位数大小，第二位数字大小...第三位数字，依次排序
# ()是比较的数字
# 12345() >12345(4)
# 1234(5) >1234() ,
# 1234(5) <1234(4),
# 1444 ms
class Solution:
    """
    @param nums: A list of non negative integers
    @return: A string
    """

    def largestNumber(self, nums):
        # write your code here
        from functools import cmp_to_key
        nums.sort(key=cmp_to_key(self.sort_key))
        res = ''
        for i in nums:
            res += str(i)
        if int(res) == 0:
            return '0'
        else:
            return res

    def sort_key(self, a, b):
        a = str(a)
        b = str(b)
        a_index, b_index = 0, 0
        while a_index < len(a) and b_index < len(b):
            if a[a_index] < b[b_index]:
                return 1
            elif a[a_index] > b[b_index]:
                return -1
            else:
                if a[a_index] == b[b_index] and a_index == len(a) - 1 and b_index == len(b) - 1:
                    return 0
                else:
                    a_index += 1
                    b_index += 1
        if a_index == len(a):
            if b[b_index] >= a[0]:
                return 1
            else:
                return -1
        elif b_index == len(b):
            if a[a_index] >= b[0]:
                return -1
            else:
                return 1
