class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        queue= deque()
        bananaCount = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    bananaCount += 1

        minutes = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue and bananaCount > 0:
            minutes += 1
            for i in range(len(queue)):
                currR,currC = queue.popleft()
                for dr,dc in directions:
                    nr , nc = currR + dr, currC + dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        bananaCount -= 1

        return minutes if not bananaCount else -1