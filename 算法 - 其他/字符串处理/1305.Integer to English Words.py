"""
1305. Integer to English Words
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.

样例
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""
class Solution:
    """
    @param num: a non-negative integer
    @return: english words representation
    """
    def numberToWords(self, num):
        # Write your code here
        n1 = ["", "One", "Two", "Three", "Four", "Five",
              "Six", "Seven", "Eight", "Nine", "Ten",
              "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
              "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        n2 = ["", "Ten", "Twenty", "Thirty", "Forty",
              "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        n3 = ['Hundred', '', 'Thousand', 'Million', 'Billion']
        res = ''
        index = 1
        if num == 0:
            return 'Zero'
        elif 0 < num < 20:
            return n1[num]
        elif 20 <= num < 100:
            return n2[num // 10] + ' ' + n1[num]
        else:
            while num != '':
                digit = int(str(num)[-3::])
                num = (str(num)[:-3:])
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