class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1

        res = -1
        s = 0

        for i in range(len(gas)):
            s += gas[i]
            if s>=cost[i]:
                s -= cost[i]
                if res<0:
                    res = i
            else:
                s = 0
                res = -1
        
        return res