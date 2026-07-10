class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # creating adjacency list
        dest = defaultdict(list)
        for fro,to in sorted(tickets,reverse=True): # reverse true makes the lower lexical one at end so we can easily pop it with O(1)
            dest[fro].append(to)

        stack = ["JFK"]
        res = []

        while stack:
            while dest[stack[-1]]:
                # we keep popping values from adj list for each src and dest
                stack.append(dest[stack[-1]].pop())
            res.append(stack.pop())
            
        return res[::-1] # reversed bought some runtime error for the tester