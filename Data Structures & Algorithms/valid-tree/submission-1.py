class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbors = {i:[] for i in range(n)}
        for x,y in edges:
            neighbors[x].append(y)
            neighbors[y].append(x)

        visit = set()
        def dfs(node,pre):
            if node in visit:
                return False

            visit.add(node)
            for neighbor in neighbors[node]:
                if neighbor!=pre: #prev node and current node are in directed loop since its undirected graph
                    if not dfs(neighbor,node): return False

            return True

        return dfs(0,-1) and len(visit)==n


