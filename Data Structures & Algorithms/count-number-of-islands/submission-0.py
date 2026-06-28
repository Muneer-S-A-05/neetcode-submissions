class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if (r,c) in visited:
                    continue
                if grid[r][c]=='1':
                    islands += 1
                    queue = deque([(r,c)])
                    while queue:
                        r,c = queue.popleft()
                        if not(0<=r<rows and 0<=c<cols) or (r,c) in visited:
                            continue
                        if grid[r][c]=='1':
                            visited.add((r,c))
                            queue.append((r+1,c))
                            queue.append((r-1,c))
                            queue.append((r,c+1))
                            queue.append((r,c-1))                        
        return islands