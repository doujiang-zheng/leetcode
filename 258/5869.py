from typing import List

class Solution:
    def maxPalindromSubsequence(self, s: List[str]) -> int:
        if len(s) == 0:
            return 0

        size = len(s)
        dp = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            dp[i][i] = 1
        
        for step in range(1, size):
            for j in range(size - step):
                if s[j] == s[j + step]:
                    dp[j][j+step] = dp[j+1][j+step-1] + 2
                else:
                    dp[j][j+step] = max(dp[j+1][j+step], dp[j][j+step-1])

        return dp[0][size-1]

    def dfs(self, s: str, vis: List[bool], i: int) -> int:
        if i >= len(s):
            s1 = [s[i] for i in range(len(s)) if vis[i]]
            s2 = [s[i] for i in range(len(s)) if not vis[i]]
            l1 = self.maxPalindromSubsequence(s1)
            l2 = self.maxPalindromSubsequence(s2)
            return l1 * l2

        vis[i] = True
        ans1 = self.dfs(s, vis, i + 1)
        vis[i] = False
        ans2 = self.dfs(s, vis, i + 1)
        return max(ans1, ans2)

    def maxProduct(self, s: str) -> int:
        vis = [False] * len(s)
        return self.dfs(s, vis, 0)


if __name__ == '__main__':
    sol = Solution()
    ss = ["leetcodecom", "bb", "accbcaxxcxx"]
    for s in ss:
        print(sol.maxProduct(s))
