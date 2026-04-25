class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        k=defaultdict(list)
        for x in strs:
            y=sorted(list(x))
            k[''.join(y)].append(x)
        return list(k.values())