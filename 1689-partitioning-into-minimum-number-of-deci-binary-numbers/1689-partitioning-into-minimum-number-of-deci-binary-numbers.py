class Solution:
    def minPartitions(self, n: str) -> int:
        answer = 0
        for i in n:
            answer = max(int(i), answer)
        return answer