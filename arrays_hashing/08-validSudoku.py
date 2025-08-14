from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """Return True if a 9x9 Sudoku board is valid."""

        sq1, sq2, sq3 = [], [], []
        row, col = [], []

        for i in range(9):
            for j in range(9):
                # Column tracking
                if board[j][i] != '.':
                    col.append(board[j][i])

                # Row tracking
                if board[i][j] != '.':
                    row.append(board[i][j])

                    # Sub-Square tracking
                    if j < 3:
                        sq1.append(board[i][j])
                    elif j < 6:
                        sq2.append(board[i][j])
                    else:  
                        sq3.append(board[i][j])

            # Check sub-boxes after each set of 3 rows
            if i in (2, 5, 8):
                if (len(sq1) != len(set(sq1)) or
                    len(sq2) != len(set(sq2)) or
                    len(sq3) != len(set(sq3))):
                    return False
                sq1.clear(), sq2.clear(), sq3.clear()

            # Check current row
            if len(row) != len(set(row)):
                return False
            row.clear()

            # Check current column
            if len(col) != len(set(col)):
                return False
            col.clear()

        return True



        
# %%
