from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        que = deque()       
        pairs = {')': '(', '}': '{', ']': '['}
        for ch in s:
            if ch in ['(', '{', '[']:
                que.append(ch)
            else:
                if len(que) and que[-1] == pairs[ch]:
                    que.pop()
                else:
                    return False
        return len(que) == 0