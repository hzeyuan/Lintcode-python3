"""
给定一个包含红，白，蓝且长度为 n 的数组，将数组元素进行分类使相同颜色的元素相邻，并按照红、白、蓝的顺序进行排序。

我们可以使用整数 0，1 和 2 分别代表红，白，蓝。

样例
给你数组 [1, 0, 1, 2], 需要将该数组原地排序为 [0, 1, 1, 2]。

挑战
一个相当直接的解决方案是使用计数排序扫描2遍的算法。

首先，迭代数组计算 0,1,2 出现的次数，然后依次用 0,1,2 出现的次数去覆盖数组。

你否能想出一个仅使用常数级额外空间复杂度且只扫描遍历一遍数组的算法？
"""


class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """

    # time:6496ms
    def sortColors(self, nums):
        # write your code here
        num_one, num_two, num_zero = 0, 0, 0
        for n in nums:
            if n == 0:
                num_zero += 1
            elif n == 1:
                num_one += 1
            else:
                num_two += 1
        nums.clear()
        for i in range(num_zero):
            nums.append(0)
        for i in range(num_one):
            nums.append(1)
        for i in range(num_two):
            nums.append(2)

    """
    # time:6282ms
    def sortColors(self, nums):
        zero = []
        one = []
        two = []
        for i in nums:
            if i ==0:
                zero.append(i)
            elif i ==1:
                one.append(i)
            else:
                two.append(i)
        nums.clear()
        nums.extend(zero+one+two)
    """
