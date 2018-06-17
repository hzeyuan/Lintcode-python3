"""
662. Guess Number Higher or Lower
我们正在玩猜数游戏。 游戏如下：
我从 1 到 n 选择一个数字。 你需要猜我选择了哪个号码。
每次你猜错了，我会告诉你这个数字是高还是低。
你调用一个预定义的接口 guess(int num)，它会返回 3 个可能的结果(-1，1或0):

样例
n = 10, 我选择了 4 (但是你不知道)
返回 4。正确！
"""
"""
The guess API is already defined for you.
@param num, your guess
@return -1 if my number is lower, 1 if my number is higher, otherwise return 0
you can call Guess.guess(num)
"""


class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess

    # time: 864ms
    def guessNumber(self, n):
        # Write your code here
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            print(mid)
            # 调用了题目给的接口
            res = Guess.guess(mid)
            if res == 0:
                return mid
            elif res == 1:
                left = mid + 1
            elif res == -1:
                right = mid - 1
