"""1206. Next Greater Element I You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements
are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not
exist, output -1 for this number.

样例
Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
"""


class Solution:
    """
    @param nums1: an array
    @param nums2: an array
    @return:  find all the next greater numbers for nums1's elements in the corresponding places of nums2
    """
    # time:1368ms
    def nextGreaterElement(self, nums1, nums2):
        # Write your code here
        m = {}
        s = []
        for i in nums2:
            while len(s) and s[-1] < i:
                m[s.pop()] = i
            s += i,
        res = []
        for i in nums1:
            res += m.get(i, -1),

        return res


s = Solution()
print(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))

