from collections import deque
from typing import List, Tuple


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix = [0]
        for el in nums:
            prefix.append(el + prefix[-1])

        ans = len(nums) + 1
        # Also maintain a monotone queue, so that prefix[last] - prefix[first] is largest.
        que = deque()
        for i, pi in enumerate(prefix):
            while len(que) > 0 and pi <= prefix[que[-1]]:
                que.pop()

            while len(que) > 0 and pi - prefix[que[0]] >= k:
                ans = min(ans, i - que[0])
                que.popleft()

            que.append(i)

        if ans > len(nums):
            return -1
        else:
            return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [[84, -37, 32, 40, 95], [77, 19, 35, 10, -14], [1], [1, 2],
            [2, -1, 2], [-3]]
    ks = [167, 19, 1, 4, 3, -10]
    for num, k in zip(nums, ks):
        print(sol.shortestSubarray(num, k))