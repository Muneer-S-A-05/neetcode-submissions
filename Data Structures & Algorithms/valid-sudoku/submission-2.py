class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        box = defaultdict(list)
        n=len(board)
        for i in range(n):
            for j in range(n):
                k = board[i][j]
                if k=='.':
                    continue
                b = (i//3,j//3)
                if k in row[i] or k in col[j] or k in box[b]:
                    print(i,j,k)
                    return False
                else:
                    row[i].append(k)
                    col[j].append(k)
                    box[b].append(k)
        return True
