"""
101. 删除排序数组中的重复数字 II
跟进“删除重复数字”：

如果可以允许出现两次重复将如何处理？
"""


class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    # 3个指针
    # time: 1064ms
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        index = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[index] != nums[i]:
                index += 1
                nums[index] = nums[i]
                count = 1
            else:
                if count >= 2:
                    continue
                else:
                    count += 1
                    index += 1
                    nums[index] = nums[i]
        return index+1
    """
    # time:1067ms
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        for i in range(len(nums) - 1, 1, -1):
            if nums[i] == nums[i - 1] == nums[i - 2]:
                nums.pop(i)

        return len(nums)
    """
