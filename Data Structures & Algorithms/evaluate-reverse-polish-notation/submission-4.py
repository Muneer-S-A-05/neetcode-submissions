class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for x in tokens:
            if x in '+-*/':
                b,a=(stack.pop()),stack.pop()
                if x=='+': stack.append(a+b)
                elif x=='-': stack.append(a-b)
                elif x=='*': stack.append(a*b)
                else : stack.append(int(a/b))
            else:
                stack.append(int(x))
            print(stack)
        res=float(stack[0])
        return int(res)