class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = []
            for j in range(9):
                if board[i][j] != '.':
                    row.append(board[i][j])
            if len(row) != len(set(row)):
                return False
        for j in range(9):
            col = []
            for i in range(9):
                if board[i][j] != '.':
                    col.append(board[i][j])
            if len(col) != len(set(col)):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = []
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        if board[r][c] != '.':
                            box.append(board[r][c])
                if len(box) != len(set(box)):
                    return False
        return True
            