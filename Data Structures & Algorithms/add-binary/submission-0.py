class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        rem = 0
        a,b = a[::-1],b[::-1]
        for i in range(max(len(a),len(b))):
            diga = ord(a[i])-ord("0") if i < len(a) else 0
            digb = ord(b[i])-ord("0") if i < len(b) else 0
            total = diga + digb + rem
            char = total%2
            res = str(char) + res
            rem = total//2
        if rem:
            res = "1" + res
        return res