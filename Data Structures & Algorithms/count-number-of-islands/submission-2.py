class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    islands += 1
                    queue = deque([(r,c)])
                    grid[r][c] = '#'

                    while queue:
                        currR,currC = queue.popleft()

                        directions = [(1,0),(-1,0),(0,1),(0,-1)]
                        for dr,dc in directions:
                            nr, nc = currR + dr, currC + dc
                            if (0<=nr<rows and 0<=nc<cols and grid[nr][nc]=='1'):
                                queue.append((nr,nc))
                                grid[nr][nc] = '#'
        return islands