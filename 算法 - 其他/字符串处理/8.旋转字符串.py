"""
8. 旋转字符串
给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)

样例
对于字符串 "abcdefg".

offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"
"""


class Solution:
    # @param s: a list of char
    # @param offset: an integer
    # @return: nothing
    # time:449ms
    def rotateString(self, s, offset):
        # write you code here
        if not offset: return
        if not s: return
        offset = offset % len(s)
        for i in range(offset):
            t = s.pop()
            s.insert(0, t)
