"""
463. 整数排序
给一组整数，按照升序排序，使用选择排序，冒泡排序，插入排序或者任何 O(n2) 的排序算法。

样例
对于数组 [3, 2, 1, 4, 5], 排序后为：[1, 2, 3, 4, 5]
"""


class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    # 冒泡排序
    # 它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
    # 走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
    # time: 1279ms
    """
    def sortIntegers(self, A):
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    A[i], A[j] = A[j], A[i]
        return A
    """

    # 选择排序
    # 选择排序 选择排序描述： 基本思想：第1趟，在待排序记录r1 ~ r[n]中选出最小的记录，将它与r1交换；
    # 第2趟，在待排序记录r2 ~ r[n]中选出最小的记录，将它与r2交换；
    # 以此类推，第i趟在待排序记录r[i] ~ r[n]中选出最小的记录，将它与r[i]交换，使有序序列不断增长直到全部排序完毕。
    # time:1267ms
    def sortIntegers(self, A):
        length = len(A)
        for i in range(length):
            min_number = i
            for j in range(i + 1, length):
                if A[min_number] > A[j]:
                    min_number = j
            A[min_number], A[i] = A[i], A[min_number]
        return A

    # 插入排序
    # 插入排序的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置后插入
    # time: 1459ms
    """
    def sortIntegers(self, A):
        length = len(A)
        for i in range(1, length):
            for j in range(i,0,-1):
                if A[j] < A[j-1]:
                    A[j-1],A[j] = A[j],A[j-1]
        return A
    """


s = Solution()
print(s.sortIntegers([5, 3, 4, 2]))
