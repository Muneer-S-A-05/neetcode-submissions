class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        k=[]
        for x in strs:
            for i in range(len(k)):
                if len(k[i])>0 and sorted(k[i][0])==sorted(list(x)):
                    k[i].append(x)
                    break
            else:
                k.append([x])
        return k