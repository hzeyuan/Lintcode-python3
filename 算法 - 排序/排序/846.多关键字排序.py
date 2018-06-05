"""
846. 多关键字排序
给定 n 个学生（ 1 到 n 编号）以及他们的考试成绩，这里有两个关键字，考试成绩以及学生学号。根据第一关键字对数组进行排序(降序)，如果第一关键字相同则根据第二关键字进行排序(升序).

样例
给出 [[2,50],[1,50],[3,100]]，
返回 [[3,100],[1,50],[2,50]]
"""


# 学习python3 sort的使用方法
# sort的参数，key,resvere
class Solution:
    """
    @param array: the input array
    @return: the sorted array
    """

    # 第一种方式
    # time:1151ms
    def multiSort(self, array):
        return sorted(array, key=lambda x: (-x[1], x[0]))

    """
    # 第二种方式
    # 若要对比前后两项需要使用cmp_to_key
    # time: 1087ms
    def multiSort(self, array):
        from functools import cmp_to_key
        return sorted(array,key=cmp_to_key(self.key_sort))
    def key_sort(self,a, b):
        if a[1] < b[1]:
            return b[1] - a[1]
        elif a[1] > b[1]:
            return b[1] - a[1]
        else:
            if a[0] <= b[0]:
                return a[0] - b[0]
            else:
                return a[0] - b[0]
    """
