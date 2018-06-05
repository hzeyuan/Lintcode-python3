"""
给一个包含n个数的整数数组S，在S中找到所有使得和为给定整数target的四元组(a, b, c, d)。

样例
例如，对于给定的整数数组S=[1, 0, -1, 0, -2, 2] 和 target=0. 满足要求的四元组集合为：

(-1, 0, 0, 1)

(-2, -1, 1, 2)

(-2, 0, 0, 2)
"""


class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    # O(n^3)
    # 1113ms
    def fourSum(self, numbers, target):
        numbers.sort()
        res = []
        for i in range(len(numbers) - 3):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            for j in range(i + 1, len(numbers) - 2):
                if j > i + 1 and numbers[j] == numbers[j - 1]:
                    continue
                left, right = j + 1, len(numbers) - 1
                t = target - numbers[i] - numbers[j]
                while left < right:

                    if numbers[left] + numbers[right] < t:
                        left += 1
                    elif numbers[left] + numbers[right] > t:
                        right -= 1
                    else:
                        if [numbers[i], numbers[j], numbers[left], numbers[right]] not in res:
                            res.append([numbers[i], numbers[j], numbers[left], numbers[right]])
                        left += 1

        return res

    """
    # 把多余的数字去掉，然后选出4个排列
    # time:1328ms
    def fourSum(self, numbers, target):
        import itertools
        setNumbers = set(numbers)
        cleanedNumbers = []
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

        if numbers.count(0) >= 4:
            cleanedNumbers.append(0)

        result = []
        combinations = list(itertools.combinations(cleanedNumbers, 4))
        for i in combinations:
            if sum(i) == target and sorted(list(i)) not in result:
                result.append(sorted(list(i)))
        return sorted(result)
    """



