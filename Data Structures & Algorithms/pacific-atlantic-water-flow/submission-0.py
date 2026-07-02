class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # we move from oceans and add points to set pacific or atlantic
        # then we pick common points as result
        rows ,cols = len(heights) , len(heights[0])
        pac, atl = set() , set()

        def dfs(r,c,visited,prevHeight):
            if not (0<=r<rows) or not (0<=c<cols) or (r,c) in visited or heights[r][c] < prevHeight:
                return
            visited.add((r,c))
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
        
        for r in range(rows):
            dfs(r,0,pac,heights[r][0]) # left side
            dfs(r,cols-1,atl,heights[r][cols-1]) # right side
        
        for c in range(cols):
            dfs(0,c,pac,heights[0][c]) # top
            dfs(rows-1,c,atl,heights[rows-1][c]) # bottom
        
        res = []
        for r in range(rows):
            for c in range(cols):
                # finding points that are reachable from both oceans
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res