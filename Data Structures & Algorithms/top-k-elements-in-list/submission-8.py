class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        r = {}
        for x in nums:
            r[x] = r.get(x,0)+1
        return sorted(r, key=lambda x : r[x])[:-k-1:-1]