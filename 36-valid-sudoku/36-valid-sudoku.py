class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
	
        def is_valid(board):
            for row in board:
                s = Counter(row)
                s["."] = 0
                if s.most_common(1)[0][1] > 1:
                    return False
            return True
		
        return is_valid(board) and \
            is_valid(zip(*board)) and \
            is_valid(
            [
                board[  x * 3  ][y * 3: y * 3 + 3] +
                board[x * 3 + 1][y * 3: y * 3 + 3] +
                board[x * 3 + 2][y * 3: y * 3 + 3]
                for x in range(3)
                for y in range(3)
            ]
        )        