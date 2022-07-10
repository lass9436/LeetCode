from heapq import heappush, heappop

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        heap = [(0, -2)]
        for i in range(len(cost)):
            while i >= 2 and i - 2 > heap[0][1]: heappop(heap)
            cost[i] += heap[0][0]
            heappush(heap, (cost[i], i))        
        return min(cost[-1], cost[-2])        