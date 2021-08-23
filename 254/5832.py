from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        ans = []
        min_flag = True
        while len(ans) < len(nums):
            if min_flag:
                ans.append(s.pop(0))
            else:
                ans.append(s.pop(-1))
            min_flag = (not min_flag)
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [[1, 2, 3, 4, 5], [6, 2, 0, 9, 7]]
    for num in nums:
        print(sol.rearrangeArray(num))