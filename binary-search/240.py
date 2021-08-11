from typing import Dict, Tuple, List


class Solution:
    def bisect_right(self, arr, target):
        lo = 0
        hi = len(arr)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m <= 0:
            return False
        n = len(matrix[0])
        if n <= 0:
            return False
        if m == 1 and n == 1:
            return matrix[0][0] == target
        if m <= 0 or n <= 0:
            return False

        col0 = [row[0] for row in matrix]
        row_idx = self.bisect_right(col0, target) - 1
        if row_idx < 0 or row_idx >= m:
            return False
        col_idx = self.bisect_right(matrix[row_idx], target) - 1
        if col_idx < 0 or col_idx >= n:
            return False
        # matrix[row_idx][0] <= target < matrix[row_idx+1][0]
        # matrix[row_idx][col_idx] <= target < matrix[row_idx][col_idx+1]
        if matrix[row_idx][col_idx] == target:
            return True

        upper_right = [row[col_idx + 1:] for row in matrix[:row_idx]]
        lower_left = [row[:col_idx + 1] for row in matrix[row_idx + 1:]]
        if self.searchMatrix(upper_right, target) or self.searchMatrix(
                lower_left, target):
            return True
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