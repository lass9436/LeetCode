from collections import deque

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        L1, L2, L3 = len(s1), len(s2), len(s3)
        if L1 + L2 != L3:
            return False
        q = deque([(0, 0)])
        visited = set((0, 0))
        answer = False
        while q:
            pos1, pos2 = q.pop()
            if pos1 < L1 and s1[pos1] == s3[pos1 + pos2] and (pos1 + 1, pos2) not in visited:
                visited.add((pos1 + 1, pos2))
                q.append((pos1 + 1, pos2))
            if pos2 < L2 and s2[pos2] == s3[pos1 + pos2] and (pos1, pos2 + 1) not in visited:
                visited.add((pos1, pos2 + 1))
                q.append((pos1, pos2 + 1))
            if pos1 + pos2 == L3:
                answer = True
                return answer
        return answer