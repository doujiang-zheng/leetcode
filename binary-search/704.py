from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        idx = lo  # arr[:idx] < target <= idx
        if idx < 0 or idx >= len(nums):
            return -1
        if nums[idx] == target:
            return idx
        return -1


if __name__ == '__main__':
    sol = Solution()
    nums = [[-1, 0, 3, 5, 9, 12], [-1, 0, 3, 5, 9, 12]]
    targets = [9, 2]
    for num, target in zip(nums, targets):
        print(sol.search(num, target))
