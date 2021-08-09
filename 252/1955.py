class Solution:
    def countSpecialSubsequences(self, nums) -> int:
        mod = 10 ** 9 + 7
        length = len(nums)
        count_pos = [0 for _ in range(length)]
        for i in range(length):
            for j in range(i):
                if nums[j] == nums[i]:
                    count_pos[i] = (count_pos[i] + count_pos[j]) % mod
                elif nums[j] == nums[i] - 1:
                    count_pos[i] = (count_pos[i] + count_pos[j]) % mod
            if nums[i] == 0:
                count_pos[i] = (count_pos[i] + 1) % mod
        ans = 0
        for i in range(length):
            if nums[i] == 2:
                ans += count_pos[i]
        return ans

if __name__ == '__main__':
    examples = [
        [0, 1, 2, 2],
        [2, 2, 0, 0],
        [0, 1, 2, 0, 1, 2]
    ]
    s = Solution()
    for example in examples:
        ans = s.countSpecialSubsequences(example)
        print(ans)