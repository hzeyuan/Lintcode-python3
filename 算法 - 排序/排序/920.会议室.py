"""
920. 会议室
给定一系列的会议时间间隔，包括起始和结束时间[[s1,e1]，[s2,e2]，…(si < ei)，确定一个人是否可以参加所有会议。

样例
给定区间=[[0,30]，[5,10]，[15,20]]，返回false。
"""


# Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    # 以起始时间排序，然后比较
    # time:1007ms
    def canAttendMeetings(self, intervals):
        # Write your code here
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i - 1].end > intervals[i].start:
                return False
        return True

