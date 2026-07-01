class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        queue= deque()
        visited = set()
        banana = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    visited.add((r,c))
                elif grid[r][c] == 1:
                    banana.add((r,c))

        minutes = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            minutes += 1
            for i in range(len(queue)):
                currR,currC = queue.popleft()
                for dr,dc in directions:
                    nr , nc = currR + dr, currC + dc
                    if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        visited.add((nr,nc))
                        banana.remove((nr,nc))
        res = minutes-1 if minutes>0 else 0
        return res if not banana else -1