class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = dict()
        
        for i in nums:
            dic[i] = 0
            
        answer = 0
        
        for i in dic:
            dic[i] = 1
            length = 1
            left = i - 1
            right = i + 1
            while right in dic and dic[right] == 0:
                dic[right] = 1
                length += 1
                right += 1
            while left in dic and dic[left] == 0:
                dic[left] = 1
                length += 1
                left -= 1
            answer = max(answer, length)
            
        return answer