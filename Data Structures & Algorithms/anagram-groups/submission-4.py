class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for x in strs:
            k=[0]*26
            for i in x:
                k[ord(i)-97]+=1
            d[tuple(k)]+=[x]
        return list(d.values())