from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        R = len(grid)
        C = len(grid[0])
        visited = [[False for _ in range(C)] for _ in range(R)]
        answer = 0
        
        for i in range(R):
            for j in range(C):
                if not visited[i][j] and grid[i][j] == 1:
                    q = deque()
                    q.append((i, j))
                    count = 0
                    visited[i][j] = True
                    while q:
                        r, c = q.popleft()
                        count += 1
                        answer = max(answer, count)
                        for k in range(4):
                            dr = r + dx[k]
                            dc = c + dy[k]
                            if 0 <= dr < R and 0 <= dc < C and not visited[dr][dc] and grid[dr][dc] == 1:
                                visited[dr][dc] = True
                                q.append((dr, dc))
                                
        return answer