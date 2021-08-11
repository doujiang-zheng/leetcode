from typing import Dict, Tuple, List


class Solution:
    def bisect_right(self, arr, target):
        # find i that arr[:i] <= x < arr[i:]
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
        n = len(matrix[0])
        col = [row[0] for row in matrix]
        idx = self.bisect_right(col, target) - 1
        if idx < 0 or idx >= m:
            return False
        col_idx = self.bisect_right(matrix[idx], target) - 1
        if col_idx < 0 or col_idx > n:
            return False
        return matrix[idx][col_idx] == target


if __name__ == '__main__':
    sol = Solution()
    matrices = [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
                [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]]
    targets = [3, 13]
    for matrix, target in zip(matrices, targets):
        print(sol.searchMatrix(matrix, target))