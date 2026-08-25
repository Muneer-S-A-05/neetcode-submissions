class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]        
        res = [0] * (len(num1)+len(num2))
        for i in range(len(num1)):
            carry = 0
            for j in range(len(num2)):
                temp =  res[i+j] + int(num1[i]) * int(num2[j]) + carry
                carry = temp//10
                res[i+j] = temp%10
            if carry:
                res[i+j+1] += carry
        res = ''.join(str(x) for x in res[::-1])
        res = res.lstrip('0')
        return res if res else "0"