"""
656. Multiply Strings
以字符串的形式给定两个非负整数 num1 和 num2，返回 num1 和 num2 的乘积。

样例
num1 和 num2 的长度都小于110。
num1 和 num2 都只包含数字 0 - 9。
num1 和 num2 都不包含任意前导零。
您不能使用任何内置的BigInteger库内方法或直接将输入转换为整数。
"""


class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return product of num1 and num2
    """
    # time:658ms
    # 利用数组，模拟乘法运算
    def multiply(self, num1, num2):
        # write your code here
        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            carry = 0
            for j in range(len(num2) - 1, -1, -1):
                # 算横向之间的进位
                res[i + j + 1] += carry + int(num1[i]) * int(num2[j])
                carry = res[i + j + 1] // 10
                res[i + j + 1] %= 10
            # 算竖向之间的进位
            res[i] = carry
        # 去除 前面的0
        while i < len(num1) + len(num2):
            if res[i] == 0:
                i += 1
            else:
                break
        res = res[i:]
        return '0' if not res else ''.join(str(i) for i in res)


s = Solution()
print(s.multiply('123', '123'))
