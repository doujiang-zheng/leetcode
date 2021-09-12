from typing import List


class Solution:
    def smallestMissingValueSubtree(self, parents: List[int],
                                    nums: List[int]) -> List[int]:
        n = len(nums)
        vis = [False for _ in range(n)]
        ans = [-1 for _ in range(n)]
        idx = [(num, i) for i, num in enumerate(nums)]
        idx = sorted(idx)
        # iterate from the least num to the largest num
        k = 0
        for i in range(1, 100001):
            pass

        for num, i in idx:
            pa = i
            while pa != -1:
                if ans[pa] == -1:
                    if num > 1:
                        ans[pa] = 1
                    else:
                        ans[pa] = num + 1
                else:
                    if ans[pa] >= num:
                        ans[pa] = num + 1
                pa = parents[pa]
        return ans


if __name__ == '__main__':
    sol = Solution()
    parents = [[-1, 0, 0, 2], [-1, 0, 1, 0, 3, 3], [-1, 2, 3, 0, 2, 4, 1]]
    nums = [[1, 2, 3, 4], [5, 4, 6, 2, 1, 3], [2, 3, 4, 5, 6, 7, 8]]
    for parent, num in zip(parents, nums):
        print(sol.smallestMissingValueSubtree(parent, num))