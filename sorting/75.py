from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnts = [0, 0, 0]
        for v in nums:
            cnts[v] += 1
        acc = [cnts[0], 0, 0]
        for i in range(1, len(cnts)):
            acc[i] = acc[i-1] + cnts[i]
        ptr = 0
        for i in range(len(nums)):
            while i >= acc[ptr]:
                ptr += 1
            nums[i] = ptr


if __name__ == '__main__':
    sol = Solution()
    nums = [[2], [2, 0, 2, 1, 1, 0], [2, 0, 1], [0], [1]]
    for num in nums:
        sol.sortColors(num)
        print(num)