class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        k=[]
        for x in strs:
            y=sorted(list(x))
            for i in range(len(k)):
                if len(k[i])>0 and sorted(k[i][0])==y:
                    k[i].append(x)
                    break
            else:
                k.append([x])
        return k