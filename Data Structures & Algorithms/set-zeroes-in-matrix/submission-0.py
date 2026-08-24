class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x = set()
        y = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    x.add(i)
                    y.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in x or j in y:
                    matrix[i][j] = 0