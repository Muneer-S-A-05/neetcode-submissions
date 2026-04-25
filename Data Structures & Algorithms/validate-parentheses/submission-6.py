class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0: return False
        stack = []
        for x in s:
            if x in '({[':
                stack.append(x)
            elif not stack:
                return False
            elif x==')' and stack[-1]=='(':
                stack.pop()
            elif x=='}' and stack[-1]=='{':
                stack.pop()
            elif x==']' and stack[-1]=='[':
                stack.pop()
            else:
                return False
        return True if not stack else False