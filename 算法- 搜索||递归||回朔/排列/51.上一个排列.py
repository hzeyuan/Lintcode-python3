class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """

    # 找到上一个排列的过程：
    # 1.从右向左找到第一个num[i]>num[i+1],记录nums[i]为n
    # 2.从右向左找到一个小于nums[i]的最大数,记为m
    # 3.交换n,m
    # 4.翻转n后面的数
    # time:1829 ms
    def previousPermuation(self, nums):
        # write your code here
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                break
        else:
            nums.reverse()
            return nums
        for j in range(len(nums) - 1, i, -1):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        length = len(nums) - 1
        while i + 1 <= length:
            nums[i + 1], nums[length] = nums[length], nums[i + 1]
            i += 1
            length -= 1
        return nums


s = Solution()
print(s.previousPermuation([1, 2, 3]))
