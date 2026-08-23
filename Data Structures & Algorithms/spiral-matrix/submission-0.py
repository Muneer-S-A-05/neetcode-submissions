class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        
        l,r = 0,len(matrix[0])-1
        t,b = 0,len(matrix)-1

        dire = [0,1]

        curr = [0,0]
        
        while l<=r and t<=b:

            while (l<=curr[1]<=r) and (t<=curr[0]<=b):
                print(curr)
                res.append(matrix[curr[0]][curr[1]])
                curr[0] += dire[0]
                curr[1] += dire[1]

            if dire == [0,1]:
                dire = [1,0]
                curr[0] += 1
                curr[1] -= 1
                t+=1
            elif dire == [1,0]:
                dire = [0,-1]
                curr[0] -= 1
                curr[1] -= 1
                r -= 1
            elif dire == [0,-1]:
                dire = [-1,0]
                curr[0] -= 1
                curr[1] += 1
                b -= 1
            else:
                dire = [0,1]
                curr[0] += 1
                curr[1] += 1
                l+=1
            print()
            print(curr)
            print()
        return res
