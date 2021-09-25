from typing import List
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        vis = [[False for _ in range(n)] for _ in range(n)]
        que = []
        que.append((matrix[0][0], 0, 0))

        for _ in range(k-1):
            val, i, j = heapq.heappop(que)
            if i + 1 < n and not vis[i + 1][j]:
                heapq.heappush(que, (matrix[i+1][j], i+1, j))
                vis[i+1][j] = True
            if j + 1 < n and not vis[i][j+1]:
                heapq.heappush(que, (matrix[i][j+1], i, j+1))
                vis[i][j+1] = True
        
        val, _, _ = heapq.heappop(que)
        return val