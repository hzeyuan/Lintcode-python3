"""
524. 左填充
实现一个leftpad库，如果不知道什么是leftpad可以看样例

样例
leftpad("foo", 5)
>> "  foo"

leftpad("foobar", 6)
>> "foobar"

leftpad("1", 2, "0")
>> "01"
"""


class StringUtils:
    """
    @param: originalStr: the string we want to append to
    @param: size: the target length of the string
    @param: padChar: the character to pad to the left side of the string
    @return: A string
    """

    def leftPad(self, originalStr, size, padChar=' '):
        # Write your code here
        return padChar * (size - len(originalStr)) + originalSt


s = StringUtils()
print(s.leftPad("foo", 5))
