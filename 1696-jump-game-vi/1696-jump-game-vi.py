from heapq import heappush, heappop

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        heap=[(0,-k)]
        for i in range(len(nums)):
            while i-heap[0][1]>k: print(heappop(heap))
            nums[i]-=heap[0][0]
            heappush(heap,(-nums[i],i))
        return nums[-1]