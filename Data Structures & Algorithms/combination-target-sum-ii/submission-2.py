class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # we sort it and use while loop to ensure no duplicates when skipping an element in second i+1
        candidates.sort()
        partial = []
        def dfs(i,total):
            if total==target:
                # send in a copy or reference will be sent which gets updated
                res.append(partial.copy())
                return
            if total>target or i>=len(candidates):
                return

            partial.append(candidates[i])
            dfs(i+1,total+candidates[i])

            partial.pop()
            # since this is case when skipping nums[i], we skip till we get to another number
            while i+1<len(candidates) and candidates[i+1]==candidates[i]:
                i+=1
            dfs(i+1,total)

        dfs(0,0)
        return res