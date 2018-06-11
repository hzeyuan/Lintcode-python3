"""

425. 电话号码的字母组合
Given a digit string excluded 01, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
"""


class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    # time:1928 ms
    def letterCombinations(self, digits):
        # write your code here
        res = []
        from itertools import product
        digit_numbers = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                         '9': 'wxyz'}
        if len(digits) == 0:
            return res
        else:
            d = set()
            for l in map(self.add_letters, product(*[digit_numbers[i] for i in digits])):
                if l not in res:
                    res.append(l)
                    d.add(l)
        return res

    def add_letters(self, letter):
        s = ''
        for i in letter:
            s += i
        return s


s = Solution()
print(s.letterCombinations('22'))


