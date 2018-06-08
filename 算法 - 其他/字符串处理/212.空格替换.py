"""
212. 空格替换
设计一种方法，将一个字符串中的所有空格替换成 %20 。你可以假设该字符串有足够的空间来加入新的字符，且你得到的是“真实的”字符长度。

你的程序还需要返回被替换后的字符串的长度。

样例
对于字符串"Mr John Smith", 长度为 13

替换空格之后，参数中的字符串需要变为"Mr%20John%20Smith"，并且把新长度 17 作为结果返回。
"""


class Solution:
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """

    # time:851 ms
    def replaceBlank(self, string, length):
        # write your code her
        black_count = 0
        new_length = length
        for i in range(length):
            if string[i] == ' ':
                black_count += 1
                new_length += 2
        i = length - 1
        while i >= 0:
            if string[i] is not ' ':
                string[i + black_count * 2] = string[i]
            else:
                string[i] = '%'
                string[i + 1] = '2'
                string[i + 2] = '0'
                i += 3
                black_count -= 1
            i -= 1
        return new_length



