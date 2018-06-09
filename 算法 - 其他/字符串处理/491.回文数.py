"""
491. 回文数
判断一个正整数是不是回文数。

回文数的定义是，将这个数反转之后，得到的数仍然是同一个数。

样例
11, 121, 1, 12321 这些是回文数。

23, 32, 1232 这些不是回文数。
"""


class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """

    # time:979 ms
    def isPalindrome(self, num):
        # write your code here
        num = str(num)
        left, right = 0, len(num) - 1
        while left < right:
            if num[left] == num[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
