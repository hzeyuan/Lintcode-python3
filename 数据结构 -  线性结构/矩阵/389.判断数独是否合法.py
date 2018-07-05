"""
389. 判断数独是否合法
请判定一个数独是否有效。

该数独可能只填充了部分数字，其中缺少的数字用 . 表示。
"""


class Solution:
    """
    @param board: the board
    @return: whether the Sudoku is valid
    """
    # time:762ms
    def isValidSudoku(self, board):
        # write your code here
        # 判断行
        for s in board:
            haxi = {}
            for i in range(len(s)):
                if s[i] not in haxi and s[i] != '.':
                    haxi[s[i]] = 1
                elif s[i] in haxi:
                    return False
        # 判断列
        for i in range(len(board)):
            haxi2 = {}
            for j in range(len(board)):
                n2 = board[j][i]
                if n2 not in haxi2 and n2 != '.':
                    haxi2[board[j][i]] = 1
                elif n2 in haxi2:
                    return False
        # 判断九宫格
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                haxi3 = {}
                for k in range(9):
                    n3 = board[i + k // 3][j + k % 3]
                    if n3 not in haxi3 and n3 != '.':
                        haxi3[n3] = 1
                    elif n3 in haxi3:
                        return False
        return True


s = Solution()
print(s.isValidSudoku(
    [".87654321", "2........", "3........", "4........", "5........", "6........", "7........", "8........",
     "9........"]))
