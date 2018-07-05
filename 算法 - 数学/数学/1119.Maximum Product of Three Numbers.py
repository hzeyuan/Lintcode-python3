"""
1119. Maximum Product of Three Numbers
Given an integer array, find three numbers whose product is maximum and output the maximum product.

样例
Example 1:

Input: [1,2,3]
Output: 6
Example 2:

Input: [1,2,3,4]
Output: 24
"""


class Solution:
    """
    @param nums: an integer array
    @return: the maximum product
    """
    # time:1065ms
    def maximumProduct(self, nums):
        # Write your code here
        nums2 = nums.copy()
        max_n = [0, 0, 0]
        min_n = []
        for j in range(3):
            for i in range(1, len(nums)):
                if nums[i - 1] >= nums[i]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]
            max_n[j] = nums[-(j + 1)]
            for i in range(1, len(nums2)):
                if nums2[i - 1] <= nums2[i]:
                    nums2[i], nums2[i - 1] = nums2[i - 1], nums2[i]
            if nums2[-(j + 1)] < 0:
                min_n.append(nums2[-(j + 1)])
        if len(min_n) == 1:
            return max_n[0] * max_n[1] * max_n[2]
        elif len(min_n) >= 2 and min_n[0] * min_n[1] > max_n[1] * max_n[2]:
            return max_n[0] * min_n[0] * min_n[1]
        return max_n[0] * max_n[1] * max_n[2]


s = Solution()
print(s.maximumProduct([-4, -5, -6, 4, 3, 2, 1]))
