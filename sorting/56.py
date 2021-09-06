from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ints = sorted(intervals)
        ans = []
        p1 = 0
        p2 = 0
        n = len(ints)
        while p2 < n:
            # assume p2 is not overlapping with the previous interval
            ans.append(ints[p2])
            while p2 < n and ints[p2][0] <= ans[p1][1]:
                # merge two overlapping intervals
                ans[p1][1] = max(ans[p1][1], ints[p2][1])
                # move to the next interval
                p2 += 1
            p1 += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    ints = [[[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 4], [4, 5]]]
    for intervals in ints:
        print(sol.merge(intervals))