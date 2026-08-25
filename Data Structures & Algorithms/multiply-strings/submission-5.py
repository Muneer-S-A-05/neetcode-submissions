class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in[num1,num2]:
            return "0"
        m = len(num1)
        n = len(num2)
        res = [0] * (m+n)
        for i in range(m):
            for j in range(n):
                temp =  res[i+j] + int(num1[m-1-i]) * int(num2[n-1-j])
                res[i+j] = temp%10
                res[i+j+1] += temp//10
        res = ''.join(str(x) for x in res[::-1])
        return res.lstrip('0')