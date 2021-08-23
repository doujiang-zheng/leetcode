from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        for s in patterns:
            if word.__contains__(s):
                ans += 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    patterns = [["a", "abc", "bc", "d"], ["a", "b", "c"], ["a", "a", "a"]]
    words = ['abc', 'aaaaabbbbb', 'ab']
    for pattern, word in zip(patterns, words):
        print(sol.numOfStrings(pattern, word))