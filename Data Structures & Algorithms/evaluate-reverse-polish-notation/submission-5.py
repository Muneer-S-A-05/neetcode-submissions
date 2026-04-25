import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # these are faster as they use C
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda l, r: int(l / r)
        }
        
        def dfs():
            token = tokens.pop()
            if token not in ops:
                return int(token)
            
            right = dfs()
            left = dfs()
            
            return ops[token](left, right)
            
        return dfs()