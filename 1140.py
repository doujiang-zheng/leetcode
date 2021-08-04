class Solution:

    # def recursive_optimal(self, piles, cur_m):
    #     cur_optimal = 0
    #     for x in range(1, 2 * cur_m + 1):
    #         cur_stone = sum(piles[:x])
    #         if x < len(piles):
    #             next_piles = piles[x:]
    #             next_m = max(x, cur_m)
    #             next_optimal = self.recursive_optimal(next_piles, next_m)
    #             next_stone = sum(next_piles) - next_optimal
    #         else:
    #             next_stone = 0
    #         if cur_stone + next_stone > cur_optimal:
    #             cur_optimal = cur_stone + next_stone
    #     return cur_optimal

    def stoneGameII(self, piles):
        num = len(piles)
        acc_sum = [piles[0] for _ in range(num)]
        for i in range(1, num):
            acc_sum[i] = acc_sum[i - 1] + piles[i]

        # At each position, we compute the optimal stones of current player.
        optimal_mat = [[0 for _ in range(num + 5)] for _ in range(num + 5)]
        # Initialization: At the last position, we always obtain all left stones.
        optimal_mat[num - 1] = [piles[-1] for _ in range(num + 5)]
        for pos in range(num - 2, -1, -1):
            for cur_m in range(1, num + 1):
                # Given (pos, cur_m), we find an optimal x with largest
                # next_pos = pos + x, next_m = max(cur_m, x), 1 <= x <= 2*m
                # sum(piles[pos:next_pos]) + sum(piles[next_pos:]) - optimal_mat[next_pos][next_m]
                # optimal_mat[pos][cur_m] = optimal_mat[pos][cur_m - 1]
                # x_end should includes the left all stones
                x_end = min(num - pos, 2 * cur_m) + 1
                for x in range(1, x_end):
                    next_pos = pos + x
                    next_m = min(max(x, cur_m), num)
                    # next_pos: maximum is num, the next player gets 0 stones
                    # next_m: maximum is num, the next player gets all left stones
                    next_optimal = optimal_mat[next_pos][next_m]
                    # cur_stone = sum(piles[pos: next_pos])
                    # next_stone = sum(piles[next_pos:]) - next_optimal
                    cur_sum = acc_sum[num - 1] - acc_sum[pos] + piles[pos]
                    cur_stone = cur_sum - next_optimal

                    # if cur_stone + next_stone > optimal_mat[pos][cur_m]:
                    #     optimal_mat[pos][cur_m] = cur_stone + next_stone
                    if cur_stone > optimal_mat[pos][cur_m]:
                        optimal_mat[pos][cur_m] = cur_stone

        return optimal_mat[0][1]


if __name__ == '__main__':
    example = [2, 7, 9, 4, 4]
    # example = [1, 2, 3, 4, 5, 100]
    # example = [77, 12, 64, 35, 28, 4, 87, 21, 20]
    sol = Solution()
    ans = sol.stoneGameII(example)
    print(ans)