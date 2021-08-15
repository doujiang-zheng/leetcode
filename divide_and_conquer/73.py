from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = -1
        col = -1
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row = i
                    col = j
                    break
        
        if row == -1 or col == -1:
            return
        
        for i in range(m):
            if i == row:
                continue
            for j in range(n):
                if j == col:
                    continue
                if matrix[i][j] == 0:
                    matrix[row][j] = 0
                    matrix[i][col] = 0

        # set rows to zero with recorded rows
        for i in range(m):
            if matrix[i][col] == 0:
                for j in range(n):
                    matrix[i][j] = 0

        # set rows to zero with recorded columns
        for j in range(n):
            if matrix[row][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

if __name__ == '__main__':
    sol = Solution()
    matrices = [
        [[1,1,1],[1,0,1],[1,1,1]]
    ]
    for matrix in matrices:
        sol.setZeroes(matrix)
        print(matrix)