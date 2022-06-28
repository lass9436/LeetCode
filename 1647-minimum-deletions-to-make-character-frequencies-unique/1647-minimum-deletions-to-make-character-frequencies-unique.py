class Solution:
    def minDeletions(self, s: str) -> int:
        dic = {}
        answer = 0
        for char in s:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        result = []
        for key in dic:
            result.append(dic[key])
        result.sort(reverse=True)
        while True:
            notChange = True
            for i in range(len(result) - 1):
                if result[i] == result[i+1] and result[i+1] != 0: 
                    result[i+1] -= 1
                    answer += 1
                    result.sort(reverse=True)
                    notChange = False
                    break
            if notChange:
                break
        return answer
        