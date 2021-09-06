from typing import List, Tuple


class Solution:
    def countLetters(self, s: str) -> Tuple:
        ans = [0] * 26
        for ch in s:
            ans[ord(ch) - ord('a')] += 1
        return tuple(ans)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = dict()
        for s in strs:
            t = self.countLetters(s)
            if t not in ans:
                ans[t] = [s]
            else:
                ans[t].append(s)
        arr = [v for k, v in ans.items()]
        return arr


if __name__ == '__main__':
    sol = Solution()
    strs = [["eat", "tea", "tan", "ate", "nat", "bat"], [""], ["a"]]
    for s in strs:
        print(sol.groupAnagrams(s))