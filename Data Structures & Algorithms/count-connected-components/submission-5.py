class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashMap = {i:[] for i in range(n)}
        for a,b in edges:
            hashMap[a].append(b)
            hashMap[b].append(a)

        visited = set()
        def dfs(node):
            if node in visited: return
            visited.add(node)
            for neighbor in hashMap[node]:
                dfs(neighbor)
        
        count = 0
        for x in range(n):
            if x not in visited:
                count+=1
                dfs(x)

        return count