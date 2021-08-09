class Solution:
    def countSpecialSubsequences(self, nums) -> int:
        mod = 10 ** 9 + 7
        length = len(nums)
        count_pos = [[0, 0, 0] for _ in range(length)]
        if nums[0] == 0:
            count_pos[0][0] = 1

        for i in range(1, length):
            i0 = count_pos[i-1][0]
            i1 = count_pos[i-1][1]
            i2 = count_pos[i-1][2]
            for k in range(3):
                count_pos[i][k] = count_pos[i-1][k]

            if nums[i] == 0:
                # before_zero_sequence
                # before_zero_sequence + 0
                # empty + 0
                count_pos[i][0] = (1 + i0 * 2) % mod
            elif nums[i] == 1:
                # before_zero_sequence + 1 
                # before_zero_one_sequence
                # before_valid_zero_one_sequence + 1
                count_pos[i][1] = (i0 + i1 * 2) % mod
            elif nums[i] == 2:
                # before_one_sequence + 2
                # before_valid_zero_one_two_sequence
                # before_valid_zero_one_two_sequence + 2
                count_pos[i][2] = (i1 + i2 * 2) % mod
            
        return count_pos[-1][2]

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