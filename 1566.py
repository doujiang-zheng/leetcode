[1,2,1,2,1,1,1,3]
2
2


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        if m > len(arr):
            return False
        for i in range(len(arr) - m + 1):
            # cnt = 1
            nxt = i + m
            match = True
            for cnt in range(1, k):
                for j in range(m):
                    if arr[cnt * m + i + j] != arr[i + j]:
                        match = False
                        break
                if not match:
                    break
        return match
