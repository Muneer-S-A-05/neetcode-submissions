# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # now time for the standard shit
        dummy = ListNode(0,head)
        groupprev = dummy

        while True:
            # returns the kth node
            kth = self.getk(groupprev,k)

            # if less than k node remains
            if not kth:
                break
            # start of next k nodes
            groupnext = kth.next

            # reversing from groupprev.next till kth
            # so prev will be the node after the kth
            prev,curr = kth.next,groupprev.next
            while curr!=groupnext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # ensuring list doesn't break off between groups
            temp = groupprev.next
            groupprev.next = kth # attaching new first to previous last
            groupprev = temp # last of the previous group
        return dummy.next
    
    def getk(self,temp,k):
        while temp and k>0:
            temp = temp.next
            k-=1
        return temp