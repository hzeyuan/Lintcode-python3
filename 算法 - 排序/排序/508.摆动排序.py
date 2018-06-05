"""
508. 摆动排序
给你一个没有排序的数组，请将原数组就地重新排列满足如下性质

nums[0] <= nums[1] >= nums[2] <= nums[3]....
样例
给出数组为 nums = [3, 5, 2, 1, 6, 4] 一种输出方案为 [1, 6, 2, 5, 3, 4]
"""


class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    # 从小到大排序
    # 观察nums[0] <= nums[1] >= nums[2] <= nums[3]>=nums[4]<=nums[5]....发现
    # 只要从第二个数字开始，交换前后两个数字的值这个式子会就变成
    # nums[0] <= nums[2] <= nums[1] <= nums[4] <= nums[3]<=nums[5]....,所以只需要把排序后的数组按要求前后交换就行了
    # 当长度为偶数时，要小心越界
    # time:1302ms
    def wiggleSort(self, nums):
        # write your code here
        nums.sort()
        for i in range(1, len(nums), 2):
            if i == len(nums) - 1:
                break
            else:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
