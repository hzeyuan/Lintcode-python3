"""
15. 全排列
给定一个数字列表，返回其所有可能的排列。

样例
给出一个列表[1,2,3]，其全排列为：

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
挑战
使用递归和非递归分别解决。
"""
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    # 方法1，直接用itertools中的
    # time:827ms
    def permute(self, nums):
        # write your code here
        import itertools
        return list(itertools.permutations(nums))