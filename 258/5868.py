from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        cnt = {}
        for rect in rectangles:
            ratio = rect[0] * 1.0 / rect[1]
            if ratio in cnt:
                cnt[ratio] += 1
            else:
                cnt[ratio] = 1
        
        ans = 0
        for k, v in cnt.items():
            ans += v * (v - 1) // 2
        return ans


if __name__ == '__main__':
    sol = Solution()
    rects = [[[4, 8], [3, 6], [10, 20], [15, 30]], [[4, 5], [7, 8]]]
    for rect in rects:
        print(sol.interchangeableRectangles(rect))
