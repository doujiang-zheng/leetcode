class Solution:
    def valid(self, i, j, m, n):
        return 0 <= i and i < m and 0 <= j and j < n

    def check(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if not vis[i][j]:
                    vis[i][j] = True
                    cnt += 1
                # BFS
                q = [(i, j)]
                while len(q) > 0:
                    ti, tj = q.pop(0)
                    for k in range(4):
                        x, y = ti + dx[k], tj + dy[k]
                        if not self.valid(x, y, m, n): continue
                        if grid[x][y] == 0: continue
                        if vis[x][y]: continue
                        vis[x][y] = True
                        q.append((x, y))
        return cnt != 1

    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        tot = sum([sum(el) for el in grid])
        if tot == 0:
            return 0
        ans = 2 ** 10

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                q = []
                for k in range(4):
                    x, y = i + dx[k], j + dy[k]
                    if not self.valid(x, y, m, n): continue
                    if grid[x][y] == 0: continue
                    q.append((x, y))
                if tot - len(q) > 1:
                    ans = min(ans, len(q))
                else:
                    ans = min(ans, len(q) + 1)
        return ans
