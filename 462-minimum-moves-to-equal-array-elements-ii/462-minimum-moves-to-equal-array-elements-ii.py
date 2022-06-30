class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid = nums[len(nums)//2]
        answer = 0
        for i in range(len(nums)):
            answer += abs(nums[i] - mid)
        return answer            