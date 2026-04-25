class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # we take value v at index i and point node i to value at index v, v2
        # index -> 0  1  
        # value -> 1  3      here node 0 points to node 3
        # thus we get a linked list where values are the node
        # so repeating value in array forms cycle in the linked list
        # beginning of loop is the repeating value
        # use slow and fast from floyd's cycle detection
        # ac to floyd, the distance from beginning of array to beginning of loop
        # is same the distance where slow and fast meet to the beginning of loop
        # not an intuitive theory

        # finding intersection of fast and slow
        slow,fast=0,0
        while True:
            # single jump
            slow=nums[slow]
            # double jump
            fast=nums[nums[fast]]
            if slow==fast:
                break

        # finding beginning of loop
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow==slow2:
                return slow