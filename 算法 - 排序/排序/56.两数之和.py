"""
56. 两数之和
给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。

你需要实现的函数twoSum需要返回这两个数的下标, 并且第一个下标小于第二个下标。注意这里下标的范围是 0 到 n-1。

样例
给出 numbers = [2, 7, 11, 15], target = 9, 返回 [0, 1].

挑战
Either of the following solutions are acceptable:

O(n) Space, O(nlogn) Time
O(n) Space, O(n) Time
"""


class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    # 暴力解法
    # time :840ms
    """
    def twoSum(self, numbers, target):
        res = [0,0]
        for i in range(len(numbers)):
            for j in range(i):
                if numbers[i] +numbers[j] ==target:
                    res[0] = j
                    res[1] = i
        return res
    """

    # 思路是从找两数相加转换成寻找减数,减数存在集合中，若找到则输出，否则就将这个减数添加到集合中
    # time:575ms
    def twoSum(self, numbers, target):
        l = {}
        res = [0, 0]
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            try:
                res[0], res[1] = l[tmp], i
                break
            except KeyError:
                l[numbers[i]] = i
        return res
