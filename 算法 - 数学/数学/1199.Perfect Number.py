"""
1199. Perfect Number
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

样例
Example:

Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
"""


class Solution:
    """
    @param num: an integer
    @return: returns true when it is a perfect number and false when it is not
    """
    # time:924 ms
    def checkPerfectNumber(self, num):
        # write your code here
        import math
        count = 1
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0 and num % i != i:
                count += i + num / i
            elif num % i == 0 and num % i == i:
                count += i
        return count == num


s = Solution()
print(s.checkPerfectNumber(6))
