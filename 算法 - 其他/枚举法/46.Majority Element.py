"""
46. Majority Element
给定一个整型数组，找出主元素，它在数组中的出现次数严格大于数组元素个数的二分之一。



样例
给出数组[1,1,1,1,2,2,2]，返回 1

挑战
要求时间复杂度为O(n)，空间复杂度为O(1)
"""


class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """

    # 贪心 O(n) 空间(1)算出哪一个是主要元素，然后在计算机主要元素的个数
    # time:1544 ms
    def majorityNumber(self, nums):
        # write your code here
        count = 0
        size = len(nums) // 2 if len(nums) % 2 == 0 else len(nums) // 2 + 1
        number = nums[0]
        for i in nums:
            if i == number:
                count += 1
            else:
                count -= 1
            if count == 0:
                number = i
                count = 1
        return number


s = Solution()
print(s.majorityNumber([2, 1, 2, 2, 2,3]))
