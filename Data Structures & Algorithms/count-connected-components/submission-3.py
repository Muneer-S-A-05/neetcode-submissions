class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashMap = {i:[] for i in range(n)}
        for a,b in edges:
            hashMap[a].append(b)
            hashMap[b].append(a)

        visited = set()
        def dfs(node,pre):
            if node in visited: return True
            visited.add(node)
            for neighbor in hashMap[node]:
                if neighbor!=pre:
                    if not dfs(neighbor,node): return False
            return True
        
        count = 0
        for x in range(n):
            if x not in visited:
                count+=1
                dfs(x,-1)

        return count