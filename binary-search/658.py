from typing import List

class Solution:
    def bisect_left(self, arr, target):
        lo = 0
        hi = len(arr)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo
    
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

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        j = self.bisect_left(arr, x) # arr[:left] < x <= arr[left:]
        i = j - 1
        # right = self.bisect_right(arr, x) # arr[:right] <= x < arr[right:]
        ans = []
        while len(ans) < k:
            # don't use updated i, j as if conditions
            if not (0 <= i < len(arr)):
                ans.append(arr[j])
                j += 1
            elif not (0 <= j < len(arr)):
                ans.append(arr[i])
                i -= 1
            elif (0 <= i < len(arr)) and (0 <= j < len(arr)):
                a, b = arr[i], arr[j]
                if abs(a - x) < abs(b - x) or (abs(a - x) == abs(b - x) and a < b):
                    ans.append(arr[i])
                    i -= 1
                else:
                    ans.append(arr[j])
                    j += 1
        return sorted(ans)

if __name__ == '__main__':
    sol = Solution()
    arrs = [[1], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
    ks = [1, 1, 4]
    xs = [1, 3, -1]
    for arr, k, x in zip(arrs, ks, xs):
        print(sol.findClosestElements(arr, k, x))