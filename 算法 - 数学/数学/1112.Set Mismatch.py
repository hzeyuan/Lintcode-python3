"""
1112. Set Mismatch
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

样例
Input: nums = [1,2,2,4]
Output: [2,3]
"""


class Solution:
    """
    @param nums: an array
    @return: the number occurs twice and the number that is missing
    """
    # time:1720ms
    def findErrorNums(self, nums):
        # Write your code here
        haxi = {}
        res = [0, 0]
        for i in nums:
            if i not in haxi:
                haxi[i] = 1
            else:
                haxi[i] += 1
        for i in range(1, len(nums)+1):
            if i not in haxi:
                res[1] = i
            elif haxi[i] >= 2:
                res[0] = i
        return res


s = Solution()
print(s.findErrorNums([1, 2, 2, 4]))
