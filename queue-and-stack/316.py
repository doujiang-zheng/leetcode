import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i

        mono_stack = collections.deque()
        mono_set = set()
        for i, ch in enumerate(s):
            while mono_stack and ch not in mono_set and ch < mono_stack[
                    -1] and i < last[mono_stack[-1]]:
                k = mono_stack.pop()
                mono_set.remove(k)
            
            if ch not in mono_set:
                mono_stack.append(ch)
                mono_set.add(ch)
        ans = ''.join([ch for ch in mono_stack])
        return ans


if __name__ == '__main__':
    sol = Solution()
    ss = ["bcabc", "cbacdcbc"]
    for s in ss:
        print(sol.removeDuplicateLetters(s))