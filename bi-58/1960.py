class Solution:
    def manacher(self, s):
        l = '#'.join(list(s))
        s = '^' + l + '$'
        pass

    def maxProduct(self, s: str) -> int:
        rl = [0 for _ in range(len(s))]
        pass


if __name__ == '__main__':
    sol = Solution()
    examples = ["ababbb", "zaaaxbbby"]
    for s in examples:
        print(sol.maxProduct(s))