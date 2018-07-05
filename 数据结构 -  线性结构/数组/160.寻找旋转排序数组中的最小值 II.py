"""
160. 寻找旋转排序数组中的最小值 II
假设一个旋转排序的数组其起始位置是未知的（比如0 1 2 4 5 6 7 可能变成是4 5 6 7 0 1 2）。

你需要找到其中最小的元素。

数组中可能存在重复的元素。

样例
给出[4,4,5,6,7,0,1,2]  返回 0
"""


class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """

    # time:1007ms
    def findMin(self, nums):
        # write your code here
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        target = nums[-1]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                right = mid - 1
            elif nums[mid] > target:
                left = mid + 1
            else:
                if left < len(nums) - 1:
                    left += 1
                else:
                    right -= 1
        return min(nums[left], nums[right])


s = Solution()
print(s.findMin([1]))
