class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # mapping of pre-requisites that need to be learned
        preMap = {i:[] for i in range(numCourses)}
        for cou,pre in prerequisites:
            preMap[cou].append(pre)

        visited = set()
        def dfs(cou):
            if cou in visited:
                return False # loop detected
            if preMap[cou] == []:
                return True # no pre reqs

            visited.add(cou)
            for pre in preMap[cou]:
                if not dfs(pre): return False
            visited.remove(cou)
            preMap[cou] = []
            return True
        
        for cou in range(numCourses):
            if not dfs(cou): return False
        return True
