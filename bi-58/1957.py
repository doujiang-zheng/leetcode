class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ''
        for char in s:
            if len(ans) >= 2 and ans[-2] == ans[-1] and ans[-1] == char:
                continue
            ans += char
        return ans


if __name__ == '__main__':
    sol = Solution()
    examples = ["leeetcode", "aaabaaaa", "aab"]
    for s in examples:
        print(sol.makeFancyString(s))
