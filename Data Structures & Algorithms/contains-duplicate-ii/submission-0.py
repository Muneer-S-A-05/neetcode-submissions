class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        
        j = 0

        while j<k:
            if nums[j] in hashmap:
                return True
            hashmap[nums[j]] = j
            j += 1
        
        while j<len(nums):
            if nums[j] in hashmap:
                if abs(hashmap[nums[j]] - j) <= k:
                    return True
            hashmap[nums[j]] = j
            j += 1
        
        return False