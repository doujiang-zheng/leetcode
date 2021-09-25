from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        vis = [False for _ in range(n)]
        color = [0 for _ in range(n)]

        for i in range(n):
            if vis[i]:
                continue

            que = deque()
            que.append(i)
            vis[i] = True
            color[i] = 0
            while len(que) > 0:
                top = que.popleft()

                for j in graph[top]:
                    if vis[j]:
                        if color[top] == color[j]:
                            return False
                        continue
                    que.append(j)
                    vis[j] = True
                    color[j] = 1 - color[top] # 0 or 1
        return True