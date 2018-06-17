"""
30. 插入区间
Given a non-overlapping interval list which is sorted by start point.

Insert a new interval into it, make sure the list is still in order and non-overlapping (merge intervals if necessary).

样例
Insert (2, 5) into [(1,2), (5,9)], we get [(1,9)].

Insert (3, 4) into [(1,2), (5,9)], we get [(1,2), (3,4), (5,9)].
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """

    # 如当前元素的右端点小于插入元素的左端点，则说明当前元素与插入元素无交并。
    # 如当前元素的左端点大于插入元素的右端点，也说明当前元素与插入元素无交并。
    # 其他情况在要么相交左边，要么相交右边，要么两边都相交

    # time:1732 ms
    def insert(self, intervals, newInterval):
        results = []
        insertPos = 0
        for interval in intervals:
            if interval.end < newInterval.start:
                results.append(interval)
                insertPos += 1
            elif interval.start > newInterval.end:
                results.append(interval)
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)
        results.insert(insertPos, newInterval)

        return results


s = Solution()
print(s.insert())
