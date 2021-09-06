from bisect import bisect_left
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = sum(nums[:3])
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         x = target - nums[i] - nums[j]
        #         k = bisect_left(nums, x, lo=j+1, hi=n)
        #         if k < n:
        #             tmp = nums[i] + nums[j] + nums[k]
        #             if abs(tmp - target) < abs(ans - target):
        #                 ans = tmp
        #         if k - 1 > j:
        #             tmp = nums[i] + nums[j] + nums[k - 1]
        #             if abs(tmp - target) < abs(ans - target):
        #                 ans = tmp
        for i in range(n):
            l = i + 1
            r = n - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == target:
                    return target
                elif tmp > target:
                    if abs(tmp - target) < abs(ans - target):
                        ans = tmp
                    r -= 1
                else:
                    if abs(tmp - target) < abs(ans - target):
                        ans = tmp
                    l += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [[-3,-2,-5,3,-4], [-1, 2, 1, -4], [0, 0, 0]]
    targets = [-1, 1, 1]
    for num, target in zip(nums, targets):
        print(sol.threeSumClosest(num, target))
