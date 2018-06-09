"""914. Flip Game You are playing the following Flip Game with your friend: Given a string that contains only these
two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a
person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

样例
Given s = "++++", after one move, it may become one of the following states:

[
  "--++",
  "+--+",
  "++--"
]
If there is no valid move, return an empty list [].
"""


class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    # time:949 ms
    def generatePossibleNextMoves(self, s):
        # write your code here
        l = []
        for i in range(len(s) - 1):
            if s[i:i + 2] == '++':
                l.append(s[0:i] + '--' + s[i + 2:])
        return l


s = Solution()
print(s.generatePossibleNextMoves("++++"))
