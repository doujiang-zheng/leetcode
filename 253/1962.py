import heapq

class Solution:
    def minStoneSum(self, piles, k: int) -> int:
        que = [-i for i in piles]
        heapq.heapify(que)
        for i in range(k):
            max_val = -heapq.heappop(que)
            next_val = max_val - (max_val // 2)
            heapq.heappush(que, -next_val)
        
        ans = 0
        while len(que) > 0:
            val = heapq.heappop(que)
            ans += (-val)
        return ans

if __name__ == '__main__':
    piles = [
        [5, 4, 9],
        [4, 3, 6, 7]
    ]
    k = [2, 3]
    sol = Solution()
    for ep, ek in zip(piles, k):
        print(sol.minStoneSum(ep, ek))