class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x : -x[1])
        answer = 0
        count = 0
        for x, y in boxTypes:
            for i in range(1, x+1):
                count += 1
                if count <= truckSize:
                    answer += y
                else:
                    return answer
        return answer