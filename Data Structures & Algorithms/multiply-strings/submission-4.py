class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        res = [0] * (m+n)
        for i in range(m):
            carry = 0
            for j in range(n):
                temp =  res[i+j] + int(num1[m-1-i]) * int(num2[n-1-j]) + carry
                carry = temp//10
                res[i+j] = temp%10
            if carry:
                res[i+j+1] += carry
        res = ''.join(str(x) for x in res[::-1])
        res = res.lstrip('0')
        return res if res else "0"