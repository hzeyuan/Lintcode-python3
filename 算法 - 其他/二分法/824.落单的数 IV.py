"""
824. 落单的数 IV
给定数组，除了一个数出现一次外，所有数都出现两次，并且所有出现两次的数都挨着。请找出找出那个出现一次的数。

样例
给出 nums = [3,3,2,2,4,5,5], 返回 4。

解释：
4 只出现了一次。
给出 nums = [2,1,1,3,3], 返回 2。

解释：
2 只出现了一次。
"""


class Solution:
    """
    @param nums: The number array
    @return: Return the single number
    """
    # time:8355ms
    def getSingleNumber(self, nums):
        # Write your code here
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == nums[mid - 1]:
                if (mid - start + 1) % 2 == 1:
                    end = mid - 2
                else:
                    start = mid + 1
            elif nums[mid] == nums[mid + 1]:
                if (end - mid + 1) % 2 == 1:
                    start = mid + 2
                else:
                    end = mid - 1
            else:
                return nums[mid]
        return nums[end]

s = Solution()
print(s.getSingleNumber([1, 1, 3, 3, 2]))
