class Solution:
    def bisect_left(self, nums, target):
        # find i, so that nums[:i] < target <= nums[i]
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def bisect_right(self, nums, target):
        # find i, so that nums[:i] <= target < nums[i]
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def searchRange(self, nums, target: int):
        left = self.bisect_left(nums, target)
        if left < 0 or left >= len(nums):
            left = -1
        if 0 <= left < len(nums) and nums[left] != target:
            left = -1

        right = self.bisect_right(nums, target) - 1
        if right < 0 or right >= len(nums):
            right = -1
        if 0 <= right < len(nums) and nums[right] != target:
            right = -1

        return [left, right]

if __name__ == '__main__':
    sol = Solution()
    nums = [[5, 7, 7, 8, 8, 10], [5, 7, 7, 8, 8, 10], []]
    targets = [8, 6, 0]
    for num, target in zip(nums, targets):
        print(sol.searchRange(num, target))