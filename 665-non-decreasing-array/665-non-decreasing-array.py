class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        change = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if change == 1:
                    return False
                if i == 1:
                    nums[i-1] = -100000
                    change += 1
                    continue
                if i == len(nums) - 1:
                    change += 1
                    continue
                if nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i-2]
                    change += 1
                elif nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i-1]
                    change +=1
                else:
                    return False
        return True if change < 2 else False
        