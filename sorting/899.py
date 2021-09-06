class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ans = s
            for i in range(1, len(s)):
                tmp = s[i:] + s[:i]
                if tmp < ans:
                    ans = tmp
        else:
            ans = ''.join(sorted(s))

        return ans 

if __name__ == '__main__':
    sol = Solution()
    ss = ['cba', 'baaca']
    ks = [1, 3]
    for s, k in zip(ss, ks):
        print(sol.orderlyQueue(s, k))