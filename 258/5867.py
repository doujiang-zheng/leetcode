class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = -1
        for i, x in enumerate(word):
            if ch == x:
                index = i
                break
        if index == -1:
            return word
        else:
            prefix = word[:index + 1][::-1] + word[index + 1:]
            return prefix


if __name__ == '__main__':
    sol = Solution()
    words = ["abcdefd", "xyxzxe", "abcd"]
    chs = ['d', 'z', 'z']
    for word, ch in zip(words, chs):
        print(sol.reversePrefix(word, ch))