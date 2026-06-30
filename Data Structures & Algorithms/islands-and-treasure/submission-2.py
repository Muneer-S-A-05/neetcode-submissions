class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    queue.append((r,c))
                    visited= {(r,c)}
        
        
        dist = 0
        while queue:
            dist += 1
            for i in range(len(queue)):
                currR,currC = queue.popleft()
                for dr,dc in directions:
                    nr,nc = currR+dr,currC+dc
                    if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and grid[nr][nc]>0:
                        queue.append((nr,nc))
                        grid[nr][nc] = dist
                        visited.add((nr,nc))
