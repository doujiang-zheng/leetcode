class Solution:
    def numberOfApples(self, r):
        xaxis = (r + 1) * (r * (r + 1) // 2)
        yaxis = (r + 1) * (r * (r + 1) // 2)
        dup = (r * (r + 1) // 2)
        return 4 * (xaxis + yaxis - dup)

    def perimeter(self, r):
        return 8 * r

    def minimumPerimeter(self, neededApples: int) -> int:
        left = 1
        right = 10 ** 8
        while left < right:
            mid = (left + right) // 2
            if self.numberOfApples(mid) < neededApples:
                left = mid + 1
            else:
                right = mid
        
        if self.numberOfApples(left) >= neededApples:
            return self.perimeter(left)
        else:
            return self.perimeter(left + 1)

if __name__ == '__main__':
    examples = [1, 13, 1000000000, 100000000000000]
    s = Solution()
    # print(s.numberOfApples(1))
    # print(s.numberOfApples(2))
    # print(s.numberOfApples(233920 // 8))
    for example in examples:
        ans = s.minimumPerimeter(example)
        print(ans)