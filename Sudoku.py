class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board = board
        
        for i in range(9):
            # 9x9
            row = {}
            colum = {}
            # 3x3
            box = {}
            box_row = 3 * (i//3)
            box_colum = 3 * (i%3)
            
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in row:
                    return False
                row[board[i][j]] = 1
                if board[j][i] != '.' and board[j][i] in colum:
                    return False
                colum[board[j][i]] = 1

                row_box = box_row + j//3
                colum_box = box_colum + j%3
                if board[row_box][colum_box] in box and board[row_box][colum_box] != '.':
                    return False
                box[board[row_box][colum_box]] = 1
        
            return True
