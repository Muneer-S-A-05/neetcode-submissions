class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # edge case
        if k==1: return nums

        res=[]
        l=r=0
        # we use monotonically decreasing queue
        # the queue will always be in descending order
        # we store index in queue so we may track with the window easily
        q = collections.deque()

        while r<len(nums):
            # if new element greater than current element
            # then pop off whole list
            # only elements that come after new num
            # that are smaller can be in queue
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            # we pop left element when it gets outside window
            if l>q[0]:
                q.popleft()
            # checking if we can start adding elements
            if r+1>=k:
                res.append(nums[q[0]])
                l+=1
            r+=1
        return res