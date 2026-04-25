class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        k=defaultdict(list)
        for x in strs:
            k[''.join(sorted(list(x)))].append(x)
        return list(k.values())