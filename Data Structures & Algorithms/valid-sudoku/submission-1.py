class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            y = [x for x in board[i] if x!='.']
            if len(y)!= len(list(set(y))):
                return False
            k = [board[0][i],board[1][i],board[2][i],board[3][i],board[4][i],board[5][i],board[6][i],board[7][i],board[8][i]]
            y = [x for x in k if x!='.']
            if len(y)!= len(list(set(y))):
                return False
        for i in range(0,7,3):
            for j in range(0,7,3):
                k = [board[i][j],board[i][j+1],board[i][j+2],board[i+1][j],board[i+1][j+1],board[i+1][j+2],board[i+2][j],board[i+2][j+1],board[i+2][j+2]]
                y = [x for x in k if x!='.']
                if len(y)!= len(list(set(y))):
                    return False
        return True

