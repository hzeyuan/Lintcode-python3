"""
388. 第k个排列
给定 n 和 k，求123..n组成的排列中的第 k 个排列。

样例
对于 n = 3, 所有的排列如下：

123
132
213
231
312
321
如果 k = 4, 第4个排列为，231.

挑战
O(n*k) in time complexity is easy, can you do it in O(n^2) or less?
"""


class Solution:
    """
    @param n: n
    @param k: the k th permutation
    @return: return the k-th permutation
    """
    # 一个一个的求下一个排列
    # time:2315 ms
    def getPermutation(self, n, k):
        # write your code here
        nums = [i for i in range(1, n+1)]
        if k == 1:
            return ''.join(str(x) for x in nums)
        else:
            for _ in range(1, k):
                for i in range(len(nums) - 2, -1, -1):
                    if nums[i] < nums[i + 1]:
                        break
                for j in range(len(nums) - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                length = len(nums) - 1
                while i + 1 <= length:
                    nums[i + 1], nums[length] = nums[length], nums[i + 1]
                    i += 1
                    length -= 1
            return ''.join(str(x) for x in nums)


s = Solution()
print(s.getPermutation(2, 2))
