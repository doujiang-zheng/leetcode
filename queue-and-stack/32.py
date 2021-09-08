from collections import deque


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = deque()
        pairs = {')': '(', '}': '{', ']': '['}
        dp = [0 for _ in range(len(s))]
        ans = 0
        for i, ch in enumerate(s):
            if ch in ['(', '{', '[']:
                stack.append((ch, i))
                dp[i] = 0
            else:
                if len(stack) > 0 and stack[-1][0] == pairs[ch]:
                    _, last = stack.pop()
                    if last > 0:
                        dp[i] = dp[last-1] + dp[i-1] + 2
                    else:
                        dp[i] = dp[i-1] + 2
                    ans = max(ans, dp[i])
                else:
                    stack.clear()
                    dp[i] = 0
        return ans


if __name__ == '__main__':
    sol = Solution()
    ss = ["()(())", "()(()", "(()", ")()())", ""]
    for s in ss:
        print(sol.longestValidParentheses(s))
