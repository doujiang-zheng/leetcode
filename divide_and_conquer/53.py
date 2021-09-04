from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cont = 0
        for i in range(len(nums)):
            if cont < 0:
                cont = nums[i]
            else:
                cont += nums[i]
            ans = max(ans, cont)
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [[-2, 1, -3, 4, -1, 2, 1, -5, 4], [1], [5, 4, -1, 7, 8]]
    for num in nums:
        print(sol.maxSubArray(num))