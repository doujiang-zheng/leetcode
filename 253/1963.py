class Solution:
    def minSwaps(self, s: str) -> int:
        min_cnt = 0
        acc_cnt = 0
        for char in s:
            if char == '[':
                acc_cnt += 1
            else:
                acc_cnt += -1
            if acc_cnt < min_cnt:
                min_cnt = acc_cnt
        swap = (1 - min_cnt) // 2
        return swap


if __name__ == '__main__':
    examples = ["][][", "]]][[[", "[]"]
    sol = Solution()
    for s in examples:
        print(sol.minSwaps(s))