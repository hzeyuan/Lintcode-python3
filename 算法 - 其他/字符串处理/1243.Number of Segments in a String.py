"""1243. Number of Segments in a String Count the number of segments in a string, where a segment is defined to be a
contiguous sequence of non-space characters.

样例
Example:

Input: "Hello, my name is John"
Output: 5
"""

import re


class Solution:
    """
    @param s: a string
    @return: the number of segments in a string
    """

    # 统计单词开头的第一个字符，因为每个单词的第一个字符前面一个字符一定是空格，利用这个特性也可以统计单词的个数
    # 653 ms
    def countSegments(self, s):
        # write yout code here  
        res = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
                res += 1
        return res


s = Solution()
print(s.countSegments("Hello, my name is John"))
