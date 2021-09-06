from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m + n - 1
        p1 = m - 1
        p2 = n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p -= 1
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p -= 1
                p2 -= 1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1


if __name__ == '__main__':
    sol = Solution()
    nums1 = [[1, 2, 3, 0, 0, 0], [1], [0]]
    ms = [3, 1, 0]
    nums2 = [[2, 5, 6], [], [1]]
    ns = [3, 0, 1]
    for n1, m, n2, n in zip(nums1, ms, nums2, ns):
        sol.merge(n1, m, n2, n)
        print(n1)