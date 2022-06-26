class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window = deque()
        cardSum = 0
        answer = 0
        n = len(cardPoints)
        if k == len(cardPoints):
            return sum(cardPoints)
        for i in range(k):
            cardSum += cardPoints[i]
        answer = cardSum
        for i in range(k):
            cardSum -= cardPoints[k-i-1]
            cardSum += cardPoints[-i-1]
            answer = max(answer, cardSum)
        return answer