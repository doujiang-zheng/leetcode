class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        begin = -1
        cnt = 0
        ans = 0
        first = -1
        for i, n in enumerate(nums):
            if n > 0:
                if cnt % 2 == 0:
                    ans = max(ans, i - begin)
                else:
                    ans = max(ans, i - first)
            elif n < 0:
                cnt += 1
                if cnt % 2 == 0:
                    ans = max(ans, i - begin)
                else:
                    ans = max(ans, i - 1 - begin)
                if first != -1:
                    first = i
            else:
                cnt = 0
                begin = i
                first = -1
        return ans
