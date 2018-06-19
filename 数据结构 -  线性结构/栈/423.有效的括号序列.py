"""
423. 有效的括号序列
给定一个字符串所表示的括号序列，包含以下字符： '(', ')', '{', '}', '[' and ']'， 判定是否是有效的括号序列。

样例
括号必须依照 "()" 顺序表示， "()[]{}" 是有效的括号，但 "([)]"则是无效的括号。
"""


class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """

    def isValidParentheses(self, s):
        # write your code here
        zhan = []
        for i in s:
            if i == '{' or i == '(' or i == '[':
                zhan.append(i)
            else:
                if not zhan:
                    return False
                if i == '}' and zhan[-1]!= '{' or i == ')' and zhan[-1] != '(' or i == ']' and zhan[-1] != '[':
                    return False
                else:
                    zhan.pop()
        return not zhan
s = Solution()
print(s.isValidParentheses('['))
