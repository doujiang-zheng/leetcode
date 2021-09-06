from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n):
            for j in range(i + 1, n):
                l = j + 1
                r = n - 1
                while l < r:
                    tmp = nums[i] + nums[j] + nums[l] + nums[r]
                    if tmp == target:
                        ans.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif tmp < target:
                        l += 1
                    else:
                        r -= 1
                # for k in range(j + 1, n):
                #     for l in range(k + 1, n):
                #         if nums[i] + nums[k] + nums[l] + nums[j] == target:
                #             ans.add((nums[i], nums[j], nums[k], nums[l]))
        arr = []
        for key in ans:
            arr.append(key) 
        return arr


if __name__ == '__main__':
    sol = Solution()
    nums = [[1, 0, -1, 0, -2, 2], [2, 2, 2, 2, 2]]
    targets = [0, 8]
    for num, target in zip(nums, targets):
        print(sol.fourSum(num, target))