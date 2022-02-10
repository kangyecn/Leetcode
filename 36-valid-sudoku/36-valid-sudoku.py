class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
	
        for i in range(9):
            col = []
            row = []
            block = []
            for j in range(9):
                c = board[i][j] # Goes columnwise
                if c != '.':
                    col.append(c)
                r = board[j][i] # Goes rowwise
                if r != '.':
                    row.append(r)
                b = board[(i//3)*3+j//3][(i%3)*3+j%3] # Goes blockwise
                if b != '.':
                    block.append(b)
            if len(col) != len(set(col)) or len(row) != len(set(row)) or len(block) != len(set(block)):
                return False
        return True   