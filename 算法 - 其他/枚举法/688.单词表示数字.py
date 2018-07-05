"""
688. 单词表示数字
给一个非负整数 n, 用单词打印数字

样例
给出 n = 125
返回 one hundred twenty five
"""


class Solution:
    """
    @param number: the number
    @return: the number in words
    """

    # time:675ms
    def convertWords(self, number):
        # Write your code here
        n1 = ["", "one", "two", "three", "four", "five",
              "six", "seven", "eight", "nine", "ten",
              "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
        n2 = ["", "ten", "twenty", "thirty", "forty",
              "fifty", "sixty", "seventy", "eighty", "ninety"]
        n3 = ['hundred', '', 'thousand', 'million', 'billion']
        res = ''
        index = 1
        if number == 0:
            return 'zero'
        elif 0 < number < 20:
            return n1[number]
        elif 20 <= number < 100:
            return n2[number // 10] + ' ' + n1[number]
        else:
            while number != '':
                digit = int(str(number)[-3::])
                number = (str(number)[:-3:])
                i = len(str(digit))
                r = ''
                while True:
                    if digit < 20:
                        r += ' ' + n1[digit] + ' '
                        break
                    elif 20 <= digit < 100:
                        r += ' ' + n2[digit // 10]
                    elif 100 <= digit < 1000:
                        r += ' ' + n1[digit // 100] + ' ' + n3[0]
                    digit = digit % (10 ** (i - 1))
                    i -= 1
                r = r.strip()
                if digit != 0 or i >= 1:
                    r += ' '+n3[index]+' '
                index += 1
                r += res
                res = r
        return res.strip()


s = Solution()
print(s.convertWords(312123))
