class Solution:
    def minSpaceWastedKResizing(self, nums, k: int) -> int:
        # Each resize operation at index i affects util the next resize
        # operation j, so that its waste is max(nums[i:j]) - sum(nums[i:j]).
        # We traverse the array nums inversely from the end to the start.
        # At each index i, we iterate over k operations, where k-th operation 
        # is only related with previous (k-1)-th operation, and we select the
        # minimum previous index (j, k-1).
        # For k=0, we initialize all indices as the same.
        # At the index 0, we have an additional resize operation, so we
        # explore the (k+1)-th operation at index 0.
        num_len = len(nums)
        acc_sum = [nums[0]]
        for i in range(1, num_len):
            acc_sum.append(acc_sum[-1] + nums[i])
        max_num = max(nums)
        min_waste = [[int(1e6 * 300) for _ in range(k + 2)] for _ in range(num_len)]
        max_waste = max_num * num_len - acc_sum[-1]
        min_waste[0][0] = max_waste

        for i in range(num_len - 1, -1, -1):
            # Suppose that we perform the step-th resize at index i.
            if i == 0:
                end_step = k + 1
            else:
                end_step = k
            for step in range(1, end_step + 1):
                if step == 1:
                    min_waste[i][step] = max(nums[i:]) * (num_len - i) - sum(nums[i:])
                    continue
                # Suppose that we perform the operation among nums[i:j].
                max_num = nums[i]
                for j in range(i + 1, len(nums)):
                    ij_sum = acc_sum[j - 1] - acc_sum[i] + nums[i]
                    cur_waste = max_num * (j - i) - ij_sum
                    cur_waste += min_waste[j][step-1]
                    if cur_waste < min_waste[i][step]:
                        min_waste[i][step] = cur_waste
                    # Update max_num
                    max_num = max(max_num, nums[j])
        
        return min_waste[0][k + 1]



if __name__ == '__main__':
    sol = Solution()
    nums = [
        [10, 20],
        [10, 20, 30],
        [10, 20, 15, 30, 20],
    ]
    ks = [0, 1, 2]
    for num, k in zip(nums, ks):
        print(sol.minSpaceWastedKResizing(num, k))