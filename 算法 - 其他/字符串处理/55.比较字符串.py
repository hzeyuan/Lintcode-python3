"""
55. 比较字符串
比较两个字符串A和B，确定A中是否包含B中所有的字符。字符串A和B中的字符都是 大写字母

样例
给出 A = "ABCD" B = "ACD"，返回 true

给出 A = "ABCD" B = "AABC"， 返回 false
"""


class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    # 计算A中字母出现的个数，储存在一个集合中
    # 计算B中字母出现的个数，在集合中减去出现的数字的次数，然后判断
    # time:1227ms
    def compareStrings(self, A, B):
        # write your code here
        # A和B都不是""
        if A and B:
            dict_a = {i: 0 for i in A}
            # 记录A中字母出现的次数
            for i in dict_a.keys():
                for a in A:
                    if i == a:
                        dict_a[i] += 1
            # B中字母出现一次，即删除A中的一个次数
            # 如果没有次数<0，说明同一个字母B中出现的次数比A多
            # 当 B中包含的字母在A中没有，会报出KeyError错误，返回False
            for b in B:
                try:
                    if dict_a[b] > 0:
                        dict_a[b] -= 1
                    else:
                        return False
                except KeyError:
                    return False
        # B不为空的话，说明A为空
        elif B:
            return False
        # 两种可能：
        # A不为空，B为空
        # A B都为空
        else:
            return True
        return True
