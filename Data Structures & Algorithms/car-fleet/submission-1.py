class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = [[p,s] for p,s in zip(position,speed)]
        ps.sort(key=lambda x:x[0])
        stack=[]
        for p,s in ps[::-1]:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-2]>=stack[-1]:
                stack.pop()
        return len(stack)

'''
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_count = 0
        curr_fleet_time = 0
        for car in sorted(range(len(position)),key=lambda i: position[i], reverse=True):
            t = (target-position[car])/speed[car]
            if t>curr_fleet_time:
                fleet_count+=1
                curr_fleet_time = t
        return fleet_count
'''