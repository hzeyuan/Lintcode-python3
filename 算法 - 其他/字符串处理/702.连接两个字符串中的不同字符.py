"""
702. 连接两个字符串中的不同字符
给出两个字符串, 你需要修改第一个字符串，将所有与第二个字符串中相同的字符删除, 并且第二个字符串中不同的字符与第一个字符串的不同字符连接

样例
给出 s1 = aacdb, s2 = gafd
返回 cbgf
给出 s1 = abcs, s2 = cxzca;
返回 bsxz
"""


class Solution:
    """
    @param s1: the 1st string
    @param s2: the 2nd string
    @return: uncommon characters of given strings
    """

    # time:906 ms
    def concatenetedString(self, s1, s2):
        # write your code here
        s = {i: 0 for i in s1}
        front, end = '', ''
        for i in s1: s[i] += 1
        for i in s2:
            if i not in s.keys():
                end += i
            else:
                s[i] = 0
        for i in s1:
            if s[i] > 0:
                front += i
        return front + end
