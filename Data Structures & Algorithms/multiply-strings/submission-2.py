class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = [num1[(i if i>-1 else 0):i+4] for i in range(len(num1)-4,-4,-4)]
        b = [num2[(i if i>-1 else 0):i+4] for i in range(len(num2)-4,-4,-4)]
        res = ["0"] * (len(a)+len(b))
        for i in range(len(a)):
            carry = 0
            for j in range(len(b)):
                temp =  int(res[i+j]) + int(a[i]) * int(b[j]) + carry
                carry = temp//10000
                temp = str(temp)
                if len(temp)>3:
                    res[i+j] = temp[len(temp)-4:len(temp)]
                else:
                    temp = "0"*(4-len(temp)) + temp
                    res[i+j] = temp
            if carry: res[i+j+1] = str(carry)
        res = ''.join(x if x!="0" else '' for x in res[::-1])
        res = res.lstrip('0')
        return res if res else "0"