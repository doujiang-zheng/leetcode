from typing import Dict, Tuple, List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == '__main__':
    sol = Solution()
    nums = [[1, 3, 5, 6], [1, 3, 5, 6], [1, 3, 5, 6], [1, 3, 5, 6], [1]]
    targets = [5, 2, 7, 0, 0]
    for num, target in zip(nums, targets):
        print(sol.searchInsert(num, target))