import bisect

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles):
        ans = [1 for _ in range(len(obstacles))]
        # for i in range(1, len(obstacles)):
        #     for j in range(i - 1, -1, -1):
        #         if obstacles[j] <= obstacles[i]:
        #             ans[i] = max(ans[j] + 1, ans[i])
        # We record the smallest value with the same length of obstacles sequence.
        # Further, the values in dp_val are ascending.
        dp_val = [int(1e8) for _ in range(len(obstacles))]
        for i in range(len(obstacles)):
            k = bisect.bisect_right(dp_val, obstacles[i])
            ans[i] = k + 1
            dp_val[k] = obstacles[i]
        return ans


if __name__ == '__main__':
    sol = Solution()
    examples = [[1, 2, 3, 2], [2, 2, 1], [3, 1, 5, 6, 4, 2]]
    for obstacles in examples:
        print(sol.longestObstacleCourseAtEachPosition(obstacles))