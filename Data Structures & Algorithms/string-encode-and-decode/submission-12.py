class Solution:
    def encode(self, strs: List[str]) -> str:
        s=''
        for i in strs:
            s+= str(len(i))+'#'+i
        return s

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            l=i
            while s[l]!='#':
                l+=1
            k = int(s[i:l])
            res.append(s[l+1:l+k+1])
            i=l+k+1
        return res
