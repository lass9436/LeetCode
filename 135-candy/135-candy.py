class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        arr = [1] * N
        for i in range(1, N):
            if ratings[i-1] < ratings[i]:
                if arr[i-1] >= arr[i]:
                    arr[i] = arr[i-1] + 1
        for i in range(N-2, -1, -1):
            if ratings[i+1] < ratings[i]:
                if arr[i+1] >= arr[i]:
                    arr[i] = arr[i+1] + 1    
        return sum(arr)
        