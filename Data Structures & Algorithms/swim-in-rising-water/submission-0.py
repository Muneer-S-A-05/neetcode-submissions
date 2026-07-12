class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        heap = [(grid[0][0],0,0)]
        res = 0
        visit = set()

        while heap:
            # we add minimum value neighbour to heap
            time,r,c = heapq.heappop(heap)
            # max value attained in such path to right bottom corner will be result
            res = max(res,time)
            if (r,c) in visit:
                continue
            visit.add((r,c))
            if (r,c) == (row-1,col-1):
                return res
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if (0<=nr<row) and (0<=nc<col) and (nr,nc) not in visit:
                    heapq.heappush(heap,(grid[nr][nc],nr,nc))
            