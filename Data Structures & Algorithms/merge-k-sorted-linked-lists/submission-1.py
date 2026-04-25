# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        heap = []

        # pushing all smallest values to min heap
        for i,l in enumerate(lists):
            if l:
                # we use value to compare element first then index
                # without index, comparison throws error if values are same
                # and we can't compare nodes directly
                heapq.heappush(heap,(l.val,i,l))
        while heap:
            # pops out smallest value
            val,i,node = heapq.heappop(heap)
            temp.next = node
            temp = temp.next
            # pushes next item in list into heap
            if node.next:
                heapq.heappush(heap,(node.next.val,i,node.next))
        return dummy.next