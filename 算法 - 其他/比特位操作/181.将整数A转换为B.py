"""
181. 将整数A转换为B
如果要将整数A转换为B，需要改变多少个bit位？

样例
如把31转换为14，需要改变2个bit位。

(31)10=(11111)2

(14)10=(01110)2
"""
"""
&	按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0	(a & b)
|	按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。	(a | b)
^	按位异或运算符：当两对应的二进位相异时，结果为1 	(a ^ b)
~	按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1	(~a )
<<	左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0。
>>	右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数 
"""


class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: An integer
    """

    # time:1310ms
    def bitSwapRequired(self, a, b):
        # write your code here
        count = 0
        # 使用异或运算符,得到一个当a和b位数不同是的值
        x = a ^ b
        for i in range(32):
            # 最右边的数字是为1,说明需要改变bit+1，最右边的数字为0,说明不用改变bit
            count += (x & 1)
            x >>= 1
            if x == 0:
                break
        return count
