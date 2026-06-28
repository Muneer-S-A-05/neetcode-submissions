class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in visited:
                    islands += 1
                    queue = deque([(r,c)])
                    visited.add((r,c))

                    while queue:
                        currR,currC = queue.popleft()

                        directions = [(1,0),(-1,0),(0,1),(0,-1)]
                        for dr,dc in directions:
                            nr, nc = currR + dr, currC + dc
                            if (0<=nr<rows and 0<=nc<cols and grid[nr][nc]=='1' and (nr,nc) not in visited):
                                queue.append((nr,nc))
                                visited.add((nr,nc))                
        return islands