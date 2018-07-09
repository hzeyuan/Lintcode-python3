"""
633. 寻找重复的数
给出一个数组 nums 包含 n + 1 个整数，每个整数是从 1 到 n (包括边界)，保证至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

样例
给出 nums = [5,5,4,3,2,1]，返回 5.
给出 nums = [5,4,4,3,2,1]，返回 4.
"""


class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    """
    # 用二分法来写，python3超时了
    def findDuplicate(self, nums):
        # write your code here
        start, end = 1, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.check_small_number(mid, nums) <= mid:
                start = mid
            else:
                end = mid
        if self.check_small_number(start,nums):
            return end
        else:
            return start

    def check_small_number(self, mid, nums):
        n = 0
        for i in range(len(nums)):
            if nums[i] <= mid:
                n += 1
        return n
    """
    # time:2844 ms
    def findDuplicate(self, nums):
        # write your code here
        haxi = {}
        for i in nums:
            if i not in haxi:
                haxi[i] = 1
            else:
                return i


s = Solution()
print(s.findDuplicate([5, 5, 4, 3, 2, 1]))
