"""
681. 缺失的第一个素数
给一个整数数组，找到最小的未出现的素数

样例
给一个数组 [2,3,5,7,11,13,17,23,29]
返回 19
"""


class Solution:
    """
    @param nums: an array of integer
    @return: the first missing prime number
    """
    # time:2970 ms
    def firstMissingPrime(self, nums):
        # write your code here
        if not nums:
            return 2
        sushu = set()
        for i in range(2, nums[-1]):
            m = 2
            while m < i:
                if i % m == 0:
                    break
                else:
                    m += 1
            if m == i:
                sushu.add(i)
        res = (sushu - set(nums))
        if not res:
            max_num = nums[-1] + 1
            while True:
                m1 = 2
                while m1 < max_num:
                    if max_num % m1 == 0:
                        break
                    else:
                        m1 += 1
                if m1 == max_num:
                    sushu.add(max_num)
                    break
                else:
                    max_num += 1
            return max_num
        else:
            return sorted(list(res))[0]



