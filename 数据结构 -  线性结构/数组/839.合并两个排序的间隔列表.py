"""
839. 合并两个排序的间隔列表
合并两个已排序的间隔列表，并将其作为一个新的排序列表返回。新的排序列表应该通过拼接两个列表的间隔并按升序排序。

样例
给定 list1 = [(1,2),(3,4)] 和 list2 = [(2,3),(5,6)], 返回 [(1,4),(5,6)].
"""


# Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """

    def mergeTwoInterval(self, list1, list2):
        # write your code here
        index1, index2 = 0, 0
        result = []
        while index1 < len(list1) and index2 < len(list2):
            if len(result) == 0 or result[-1].end < list1[index1].start:
                result.append(list1[index1])
                index1 += 1
            else:
                result[-1].end = max(result[-1].end, list1[index1].end)
                index1 += 1

            if result[-1].end < list2[index2].start:
                # result.append(list2[index2])
                index2 += 1
            else:
                result[-1].end = max(result[-1].end, list2[index2].end)
                index2 += 1
        return result


s = Solution()
a = Interval(1, 3)
b = Interval(3, 4)
c = Interval(5, 6)
d = Interval(7, 8)
print(s.mergeTwoInterval([a, b], [c, d]))
