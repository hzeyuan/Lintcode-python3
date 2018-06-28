"""
100. 删除排序数组中的重复数字
给定一个排序数组，在原数组中删除重复出现的数字，使得每个元素只出现一次，并且返回新的数组的长度。

不要使用额外的数组空间，必须在原地没有额外空间的条件下完成。

样例
给出数组A =[1,1,2]，你的函数应该返回长度2，此时A=[1,2]。
"""


class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """

    # time:779 ms
    def removeDuplicates(self, nums):
        # write your code here
        if not nums:
            return 0
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1
    """
    # time:1166ms
    def removeDuplicates(self, nums):
    if not nums:
        return  0
    
    for i in range(len(nums)-1,0,-1):
        if nums[i] == nums[i-1]:
            nums.pop(i)
            
    return len(nums)
    """

s = Solution()
a =[-14, -14, -13, -13, -13, -13, -13, -13, -13, -12, -12, -12, -12, -11, -10, -9, -9, -9, -8, -7, -5, -5, -5, -5, -4,
     -3, -3, -2, -2, -2, -2, -1, -1, -1, -1, -1, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 8,
     8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 13, 14, 14, 14, 14, 15, 16, 16, 16, 18, 18, 18, 19, 19, 19, 19,
     20, 20, 20, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 23, 23, 24, 25, 25]
print(s.removeDuplicates(a))
print(a)
