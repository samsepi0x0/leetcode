class Solution:
    def isValid(self, arr : List[str]) -> bool:
        res = [i for i in arr if i != '.']
        return len(res) == len(set(res))
    
    def check_row_or_col(self, board: List[List[str]]) -> bool:
        for i in board:
            if not self.isValid(i):
                return False
        return True
            
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        arr = []
        #Check Validity of Rows
        if not self.check_row_or_col(board):
            return False
        print()
        #Transpose the matrix
        for i in range(0, len(board)):
            for j in range(i+1, len(board)):
                board[i][j], board[j][i] = board[j][i], board[i][j]
        
        #Check Validity opf Cols
        if not self.check_row_or_col(board):
            return False
        
        #Check Validity of Square
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                arr = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.isValid(arr):
                    return False
        return True
