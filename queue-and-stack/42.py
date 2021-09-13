from typing import List
from collections import deque

class Solution:
    def trap(self, height: List[int]) -> int:
        # We only have to find left_max and right_max to compute how
        # much rain can be stored at current elevation level.
        # In such way, we maintain a decreasing monotone stack.
        stack = deque()
        ans = 0
        for i, h in enumerate(height):
            while len(stack) > 0 and h > height[stack[-1]]:
                pre_j = stack.pop()
                if len(stack) == 0:
                    break
                left_max = stack[-1]
                distance = i - left_max - 1
                bounded_height = min(height[left_max], h) - height[pre_j]
                ans += distance * bounded_height
            stack.append(i)
        return ans


if __name__ == '__main__':
    sol = Solution()
    heights = [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], [4, 2, 0, 3, 2, 5]]
    for height in heights:
        print(sol.trap(height))