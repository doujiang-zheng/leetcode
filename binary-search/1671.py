from typing import List


class Solution:
    def longestIncreasingSubsequence(self, nums):
        cnt = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    cnt[i] = max(cnt[i], cnt[j] + 1)
        return cnt

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        length = len(nums)
        left_cnt = self.longestIncreasingSubsequence(nums)
        inv_nums = [nums[length - i - 1] for i in range(length)]
        right_cnt = self.longestIncreasingSubsequence(inv_nums)[::-1]
        ans = length
        for i in range(length):
            if left_cnt[i] >= 2 and right_cnt[i] >= 2:
                ans = min(ans, length - (left_cnt[i] + right_cnt[i] - 1))
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [[100, 92, 89, 77, 74, 66, 64, 66, 64],
            [9, 8, 1, 7, 6, 5, 4, 3, 2, 1], [1, 3, 1],
            [2, 1, 1, 5, 6, 2, 3, 1], [4, 3, 2, 1, 1, 2, 3, 1],
            [1, 2, 3, 4, 4, 3, 2, 1]]
    for num in nums:
        print(sol.minimumMountainRemovals(num))
    pass