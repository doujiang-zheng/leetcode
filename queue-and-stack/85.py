from typing import List
import collections


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0:
            return 0

        # This problem is a 2D 84:Largest Rectangle in Histogram.
        r, c = len(matrix), len(matrix[0])
        rows = [[0 for _ in range(c)] for _ in range(r)]
        cols = [[0 for _ in range(c)] for _ in range(r)]
        # for i in range(r):
        #     rows[i][0] = 1 if matrix[r][0] == '1' else 0
        #     for j in range(1, c):
        #         if matrix[i][j] == '1':
        #             rows[i][j] = 1 + rows[i][j-1]
        
        for j in range(c):
            cols[0][j] = 1 if matrix[0][j] == '1' else 0
            for i in range(1, r):
                if matrix[i][j] == '1':
                    cols[i][j] = 1 + cols[i-1][j]
        
        left_inc = [list(range(c)) for _ in range(r)]
        right_inc = [list(range(c)) for _ in range(r)]

        for i in range(r):
            stack = collections.deque()
            for j in range(c):
                while stack and cols[i][j] <= cols[i][stack[-1]]:
                    stack.pop()
                
                if len(stack) > 0:
                    left_inc[i][j] = stack[-1] + 1
                else:
                    left_inc[i][j] = 0
                stack.append(j)
        
        for i in range(r):
            stack = collections.deque()
            for j in range(c-1, -1, -1):
                while stack and cols[i][j] <= cols[i][stack[-1]]:
                    stack.pop()
                
                if len(stack) > 0:
                    right_inc[i][j] = stack[-1] - 1
                else:
                    right_inc[i][j] = c-1
                stack.append(j)
                
        area = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                # assume matrix[i][j] is the lower-right cell
                area[i][j] = cols[i][j] * (right_inc[i][j] - left_inc[i][j] + 1)

        ans = max([max(area[i]) for i in range(r)])
        return ans


if __name__ == '__main__':
    sol = Solution()
    matrices = [[['1', '1']],
        [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
         ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]],
        [],
        [["0"]],
        [["1"]],
        [["0", "0"]],
    ]
    for matrix in matrices:
        print(sol.maximalRectangle(matrix))