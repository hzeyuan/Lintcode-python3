"""
1178. Student Attendance Record I
You are given a string representing an attendance record for a student. The record only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

样例
Example 1:

Input: "PPALLP"
Output: True
Example 2:

Input: "PPALLL"
Output: False
"""


class Solution:
    """
    @param s: a string
    @return: whether the student could be rewarded according to his attendance record
    """

    # time: 1858 ms
    def checkRecord(self, s):
        # Write your code here
        attendance_record = {'A':0,'L':0,"P":0}
        for i in s :
            attendance_record[i] +=1
        if attendance_record['A'] >=2 or 'LLL'in s:
            return False
        return True
