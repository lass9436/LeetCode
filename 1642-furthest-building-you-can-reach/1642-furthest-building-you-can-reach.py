from heapq import heappop, heappush

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        reqBri = 0
        N = len(heights)
        for i in range(1, N):
            hei = heights[i] - heights[i-1]
            if hei > 0:
                if ladders == len(heap):
                    if ladders and heap[0] < hei:
                        reqBri += heappop(heap)
                        heappush(heap, hei)
                    else:
                        reqBri += hei
                else:
                    heappush(heap, hei)
            if reqBri > bricks:
                return i-1
        return N-1    