class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flight = [float('inf')]*n
        flight[src] = 0

        for i in range(k+1):
            temp = flight.copy()

            for s,d,p in flights:
                if flight[s] == float('inf'):
                    continue
                if flight[s] + p < temp[d]:
                    temp[d] = flight[s] + p
            flight = temp

        return flight[dst] if flight[dst] != float('inf') else -1