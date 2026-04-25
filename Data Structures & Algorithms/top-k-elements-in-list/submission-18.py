class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        r = {}
        freq=[[] for i in range(len(nums)+1)]
        for i in nums:
            r[i] = r.get(i,0)+1
        for x,c in r.items():
            freq[c].append(x)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res