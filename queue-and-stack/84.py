from typing import List
from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # ans = 0

        # n = len(heights)
        # for i in range(n):
        #     cur_min = heights[i]
        #     for j in range(i, -1, -1):
        #         cur_min = min(cur_min, heights[j])
        #         ans = max(ans, cur_min * (i - j + 1))

        # for each bar i, we explore its left most neighbor left_inc,
        # so that heights[left_inc:i] >= heights[i] and 
        # heights[left_inc-1] < heights[i]. We do the same thing for the
        # right most neighbot right_inc. Then the biggest rectangle area
        # centered at bar i is heights[i] * (right_inc - left_inc +1).

        n = len(heights)
        # we maintain a monotone increasing stack, where heights[i-1] removes
        # bars higher than it.
        left_inc = list(range(n))
        stack = deque()
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            
            if len(stack) > 0:
                left_inc[i] = stack[-1] + 1 # the left most higher one
            else:
                left_inc[i] = 0

            stack.append(i)


        right_inc = list(range(n))
        stack = deque()
        for i in range(n-1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            
            if len(stack) > 0:
                right_inc[i] = stack[-1] - 1 # the right most higher one
            else:
                right_inc[i] = n - 1
            stack.append(i)
        
        ans = 0
        for i in range(n):
            ans = max(ans, heights[i] * (right_inc[i] - left_inc[i] + 1))
        return ans

if __name__ == '__main__':
    sol = Solution()
    heights = [[1, 1], [2, 0, 2], [2, 1, 5, 6, 2, 3], [2, 4]]
    for height in heights:
        print(sol.largestRectangleArea(height))