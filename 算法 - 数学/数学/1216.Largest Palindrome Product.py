"""
1216. Largest Palindrome Product
Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

样例
Input: 2
Output: 987
Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
"""


class Solution:
    """
    @param n: the number of digit
    @return: the largest palindrome mod 1337
    """

    # 直接遍历会超时
    # 正常的思路是两个n位数从大到小相乘，然后判断是不是回文数，找到后%1337输出
    # 这里的方法是：将一个n位数的翻转，然后拼接在一起构建成回文数，在爬断它是否能整除一个n位数，可以的话输出。
    def largestPalindrome(self, n):
        # write your code here
        if n == 1:
            return 9
        number = 10 ** n - 1
        for i in range(number, number // 10, -1):
            string = int(str(i) + str(i)[::-1])
            j = number
            while j * j >= string:
                if string % j == 0:
                    return string % 1337
                j -= 1



s = Solution()
print(s.largestPalindrome(7))
