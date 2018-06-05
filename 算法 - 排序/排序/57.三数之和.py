"""
给出一个有n个整数的数组S，在S中找到三个整数a, b, c，找到所有使得a + b + c = 0的三元组。

样例
如S = {-1 0 1 2 -1 -4}, 你需要返回的三元组集合的是：

(-1, 0, 1)

(-1, -1, 2
"""


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    """
     # 暴力遍历
    # time:1862ms
    def threeSum(self, numbers):
        # write your code here
        
        res = []
        for k in range(len(numbers)-2):
            for i in range(k+1,len(numbers)):
                for j in range(i+1,len(numbers)):
                    if numbers[i] + numbers[j] == -numbers[k]:
                        array = sorted([numbers[i], numbers[j], numbers[k]])
                        if res.count(array) == 0:
                            res.append(array)
        return res
    """
    """
    # 内存溢出，原因还不清楚
     def threeSum(self, numbers):
        from itertools import combinations
        res = []
        for i in list(combinations(numbers, 3)):
            if sum(i) == 0:
                k = sorted(i)
                if res.count(k) == 0:
                    res.append(k)
        return res
    """
    # 先排序列表，选取一个元素
    # 然后从左右两边开始寻找
    # time:906ms
    def threeSum(self, numbers):
        numbers.sort()
        res = []
        for n in range(len(numbers) - 2):
            left, right = n + 1, len(numbers) - 1
            while True:
                numbers_sum = numbers[n] + numbers[left] + numbers[right]
                if numbers_sum > 0:
                    right -= 1
                elif numbers_sum < 0:
                    left += 1
                else:
                    if [numbers[n], numbers[left], numbers[right]] not in res:
                        res.append([numbers[n], numbers[left], numbers[right]])
                    left += 1
                if left >= right or len(numbers) == 3:
                    break
        return res