"""
1256. Nth Digit
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

样例
Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""


class Solution:
    """
    @param n: a positive integer
    @return: the nth digit of the infinite integer sequence
    """
    # time: 920ms
    def findNthDigit(self, n):
        # write your code here
        length, cnt, start = 1, 9, 1
        while n > length * cnt:
            n -= length * cnt
            length += 1
            cnt *= 10
            start *= 10
        start += (n - 1) // length
        res = str(start)
        return int(res[(n - 1) % length])


s = Solution()
print(s.findNthDigit(11))
