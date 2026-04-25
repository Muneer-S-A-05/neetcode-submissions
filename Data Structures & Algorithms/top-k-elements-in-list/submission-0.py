class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        r = defaultdict(int)
        for x in nums:
            r[str(x)] = r[str(x)]+1
        return sorted(r.keys(), key=lambda x : r[x], reverse=True)[:k]