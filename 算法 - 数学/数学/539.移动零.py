"""
539. 移动零
给一个数组 nums 写一个函数将 0 移动到数组的最后面，非零元素保持原数组的顺序

样例
给出 nums = [0, 1, 0, 3, 12], 调用函数之后, nums = [1, 3, 12, 0, 0].
"""


class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    # 双指针，用j记录当前第一个'0'要方的位置
    # 遍历整个数组，遇到非0的数字就和j位置的交换
    # 同时，j要+1,代表下一个零要放的位置
    # time:1386 ms
    def moveZeroes(self, nums):
        # write your code here
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


s = Solution()
a = [0, 1, 0, 3, 12]
print(s.moveZeroes(a))
print(a)
