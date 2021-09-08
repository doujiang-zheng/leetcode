import heapq
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque()
        ans = []
        for i in range(len(nums)):
            # remain the que as a decreasing order
            while len(que) > 0 and nums[i] > nums[que[-1]]:
                que.pop()
            que.append(i)
            # remove elements out of range
            if i - que[0] >= k:
                que.popleft()
            if i >= k - 1:
                ans.append(nums[que[0]])
        return ans

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        que = []
        ans = []
        for i in range(len(nums)):
            # remove elements out of range
            while len(que) > 0 and i - que[0][1] >= k:
                heapq.heappop(que)
            # update with current element
            heapq.heappush(que, (-nums[i], i))
            if i >= k - 1:
                ans.append(-que[0][0])
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [
[9,10,9,-7,-4,-8,2,-6], [1, 3, 1, 2, 0, 5], [1, 3, -1, -3, 5, 3, 6, 7], [1], [1, -1],
            [9, 11], [4, -2]]
    ks = [5, 3, 3, 1, 1, 2, 2]
    for num, k in zip(nums, ks):
        print(sol.maxSlidingWindow(num, k))
        print(sol.maxSlidingWindow2(num, k))