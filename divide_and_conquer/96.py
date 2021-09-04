class Solution:
    def numTrees(self, n: int) -> int:
        nums = [1, 1]
        for i in range(2, n + 1):
            ans = 0
            for p in range(1, i + 1):
                ans += nums[p-1] * nums[i-p]
            nums.append(ans)
        return nums[n]

if __name__ == '__main__':
    sol = Solution()
    ns = list(range(1, 20))
    for n in ns:
        print(sol.numTrees(n))

