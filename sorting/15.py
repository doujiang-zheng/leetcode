import bisect
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        keys = set()
        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            x = -nums[i]
            while l < r:
                if nums[l] + nums[r] == x:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif nums[l] + nums[r] > x:
                    r -= 1
                else:
                    l += 1
                

        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [[-1,0,1,2,-1,-4,-2,-3,3,0,4], [-1, 0, 1, 2, -1, -4], [], [0]]
    for num in nums:
        print(sol.threeSum(num))