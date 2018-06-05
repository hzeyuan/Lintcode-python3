"""
给定一个有n个对象（包括k种不同的颜色，并按照1到k进行编号）的数组，将对象进行分类使相同颜色的对象相邻，并按照1,2，...k的顺序进行排序。

样例
给出colors=[3, 2, 2, 1, 4]，k=4, 你的代码应该在原地操作使得数组变成[1, 2, 2, 3, 4]

挑战
一个相当直接的解决方案是使用计数排序扫描2遍的算法。这样你会花费O(k)的额外空间。你否能在不使用额外空间的情况下完成？
"""


class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    # 这道题k好像没用到,直接套用快排模板就行了
    # time:764ms
    def sortColors2(self, colors, k):
        # write your code here

        self.quick_sort(colors, 0, len(colors) - 1)

    def quick_sort(self, Array, left, right):
        if left >= right:
            return
        low, high = left, right
        key = Array[low]
        while left < right:
            while left < right and Array[right] > key:
                right -= 1
            Array[left] = Array[right]
            while left < right and Array[left] <= key:
                left += 1
            Array[right] = Array[left]
        Array[right] = key
        self.quick_sort(Array, low, left - 1)
        self.quick_sort(Array, left + 1, high)