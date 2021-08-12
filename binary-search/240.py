from typing import Dict, Tuple, List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Two pointer
        m = len(matrix)
        n = len(matrix[0])

        i, j = 0, n - 1
        while (0 <= i < m) and (0 <= j < n):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False


if __name__ == '__main__':
    sol = Solution()
    matrices = [[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
                 [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
                [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
                 [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]]
    targets = [5, 20]
    for matrix, target in zip(matrices, targets):
        print(sol.searchMatrix(matrix, target))
    pass