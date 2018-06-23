"""
1173. Reverse Words in a String III
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

样例
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""


class Solution:
    """
    @param s: a string
    @return: reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order
    """
    # time:1770 ms
    def reverseWords(self, s):
        # Write your code here
        s = s.split(' ')
        string = ''
        for i in range(len(s) - 1):
            string += s[i][::-1] + ' '
        string += s[-1][::-1]
        return string
