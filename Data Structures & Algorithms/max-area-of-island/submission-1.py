class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    area = 1
                    grid[r][c]=2
                    queue = deque([(r,c)])

                    directions = [(1,0),(-1,0),(0,1),(0,-1)]
                    while queue:
                        currR,currC = queue.popleft()
                        for dr,dc in directions:
                            nr,nc = dr+currR, dc+currC
                            if 0<=nr<rows and 0<=nc<cols and (nr,nc)and grid[nr][nc]==1:
                                area += 1
                                grid[nr][nc] = 2
                                queue.append((nr,nc))
                    res = max(res,area)
        return res
