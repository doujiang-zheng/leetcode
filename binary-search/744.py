from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lo = 0
        hi = len(letters)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if letters[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        if lo == len(letters):
            return letters[0]

        return letters[lo]


if __name__ == '__main__':
    sol = Solution()
    letters = [
        ["c", "f", "j"],
        ["c", "f", "j"],
        ["c", "f", "j"],
        ["c", "f", "j"],
        ["c", "f", "j"],
    ]
    targets = ['a', 'c', 'd', 'g', 'j']
    for letter, target in zip(letters, targets):
        print(sol.nextGreatestLetter(letter, target))