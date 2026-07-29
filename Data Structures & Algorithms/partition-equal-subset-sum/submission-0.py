class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums)<2 or sum(nums)%2==1: return False
        target = sum(nums)//2

        dp = set([0])

        for x in nums[::-1]:
            if x == target: return True
            dpp = set(dp)
            for s in dp:
                if x+s == target:
                    return True
                dpp.add(x+s)
            dp = set(dpp)
        return False
                
