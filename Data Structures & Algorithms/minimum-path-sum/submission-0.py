class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # we calculate cost from destination to every other cell
        # we initially set all value to inf and add padding to right and bottom
        res = [[float('infinity')]*(cols+1) for i in range(rows+1)]
        res[rows][cols-1] = 0 # point below destination so cost will be zero
        # cost be taken as value of grid ele + min of below element and right element

        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                # adding grid[i][j] as cost is the grid value
                res[i][j] = grid[i][j] + min(res[i+1][j],res[i][j+1])

        return res[0][0]