class Solution:
    def rob(self, nums: List[int]) -> int:
        # we exclude first element in one set and second element in the other set since its circular
        # we add nums[0] in max func for single array edge case
        return max(nums[0],self.robber(nums[1:]),self.robber(nums[:-1]))
    
    def robber(self,nums):
        # initial values (pre array)
        rob1,rob2 = 0,0

        for x in nums:
            newrob = max(rob1 + x, rob2) # we just robbed rob2 so we only add x to rob1
            rob1,rob2 = rob2, newrob
        
        # rob2 has last maximum rob
        return rob2