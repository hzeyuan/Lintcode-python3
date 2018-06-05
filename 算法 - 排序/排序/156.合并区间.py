"""
156. 合并区间
给出若干闭合区间，合并所有重叠的部分。

样例
Given intervals => merged intervals:

[                     [
  (1, 3),               (1, 6),
  (2, 6),      =>       (8, 10),
  (8, 10),              (15, 18)
  (15, 18)            ]
]
挑战
O(n log n) 的时间和 O(1) 的额外空间。
"""


# Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval

    # 思路是先按照interval.start进行排序
    # 遍历然后比较前后的interval.end和interval.start,处理后添加到一个列表中
    # time:1225ms
    def merge(self, intervals):
        result = []
        for interval in sorted(intervals, key=lambda x: x.start):
            if len(result) == 0 or result[-1].end < interval.start:
                result.append(interval)
            else:
                result[-1].end = max(result[-1].end, interval.end)
        return result
