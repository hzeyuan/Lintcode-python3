"""
52. 下一个排列
给定一个整数数组来表示排列，找出其之后的一个排列。

样例
给出排列[1,3,2,3]，其下一个排列是[1,3,3,2]

给出排列[4,3,2,1]，其下一个排列是[1,2,3,4]
"""


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """

    # 找下一个排列的过程：
    # 1.从右向左找到第一个num[i]<nums[i+1], 记录nums[i]为n
    # 2.2.从右向左找到一个大于nums[i]的最大数,记为m
    # 3.交换n,m
    # 4.翻转n后面的数
    # time:2013 ms
    def nextPermutation(self, nums):
        # write your code here
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break
        else:
            nums.reverse()
            return nums
        for j in range(len(nums) - 1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        length = len(nums) - 1
        while i + 1 <= length:
            nums[i + 1], nums[length] = nums[length], nums[i + 1]
            i += 1
            length -= 1
        return nums


s = Solution()
print(s.nextPermutation([1, 2, 4, 2]))
