"""
1104. Judge Route Circle
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place finally.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

样例
Example 1:

Input: "UD"
Output: true
Example 2:

Input: "LL"
Output: false
"""


class Solution:
    """
    @param moves: a sequence of its moves
    @return: if this robot makes a circle
    """

    # time: 965 ms
    def judgeCircle(self, moves):
        # Write your code here
        move = {'U': 0, 'D': 0, 'L': 0, 'R': 0}
        for i in moves:
            move[i] += 1
        if move['U'] == move['D'] and move['L'] == move['R']:
            return True
        else:
            return False
