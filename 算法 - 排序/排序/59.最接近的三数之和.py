"""
给一个包含 n 个整数的数组 S, 找到和与给定整数 target 最接近的三元组，返回这三个数的和。

样例
例如 S = [-1, 2, 1, -4] and target = 1. 和最接近 1 的三元组是 -1 + 2 + 1 = 2.

挑战
O(n^2) 时间, O(1) 额外空间。
"""


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    # 方式一
    # 排序
    # 用一个变量保存最接近的值.然后二分查找，找到更小的则替换变量的值
    # time:1409ms
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        # first method
        numbers.sort()
        minNumber = numbers[0] + numbers[1] + numbers[2]
        for i in range(len(numbers) - 2):
            left, right = i + 1, len(numbers) - 1
            while left<right:
                nb = numbers[i] + numbers[left] + numbers[right]
                if abs(nb - target) <= abs(minNumber - target):
                    minNumber = nb
                    left += 1
                else:
                    right -= 1
        return minNumber
    """

    # 方式二，清洗数据，然后排列
    # time:936ms
    def threeSumClosest(self, numbers, target):
        # second method
        import itertools
        cleanedNumbers = []
        setNumbers = set(numbers)
        for i in setNumbers:
            if numbers.count(i) >= 3:
                cleanedNumbers.append(i)
                cleanedNumbers.append(i)
                cleanedNumbers.append(i)
            elif numbers.count(i) == 2:
                cleanedNumbers.append(i)
                cleanedNumbers.append(i)
            else:
                cleanedNumbers.append(i)

        combinations = list(itertools.combinations(cleanedNumbers, 3))
        minNumber = sum(combinations[0])
        for i in combinations:
            if abs(sum(i) - target) < abs(minNumber - target):
                minNumber = sum(i)

        return minNumber
