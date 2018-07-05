"""
608. Two Sum II - Input array is sorted
给定一个已经 按升序排列 的数组，找到两个数使他们加起来的和等于特定数。
函数应该返回这两个数的下标，index1必须小于index2。注意返回的值不是 0-based。

样例
给定数组为 [2,7,11,15] ，target = 9
返回 [1,2]
"""


class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    # time:1006ms
    def twoSum(self, nums, target):
        l = {}
        res = [0, 0]
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in l:
                res[0], res[1] = l[tmp], i + 1
                break
            else:
                l[nums[i]] = i + 1
        return res
