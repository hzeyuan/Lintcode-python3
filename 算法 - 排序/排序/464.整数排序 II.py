"""
464. 整数排序 II
给一组整数，按照升序排序。使用归并排序，快速排序，堆排序或者任何其他 O(n log n) 的排序算法。

样例
给出 [3, 2, 1, 4, 5], 排序后的结果为 [1, 2, 3, 4, 5]。
"""


class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    # 快速排序 方式一
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

    # 快速排序 方式二
    def quick_sort2(self, array, l, r):
        if l < r:
            q = self.partition(array, l, r)
            self.quick_sort2(array, l, q - 1)
            self.quick_sort2(array, q + 1, r)

    def partition(self, array, l, r):
        x = array[r]
        i = l - 1
        for j in range(l, r):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[r] = array[r], array[i + 1]
        return i + 1

    def sortIntegers2(self, A):
        # write your code here
        self.quick_sort(A, 0, len(A) - 1)


s = Solution()
a = [3,8, 2, 6, 1, 5, 9]
print(s.quick_sort(a, 0, len(a) - 1))
print(a)
