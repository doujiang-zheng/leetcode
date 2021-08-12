class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x^13 = x^{1101} = x^8 * x^4 * x^1
        if n < 0:
            x = 1.0 / x
            n = -n
        ans = 1
        pow = x
        while n > 0:
            if n & 1 == 1:
                ans *= pow
            n = n >> 1
            pow = pow ** 2
        return ans

if __name__ == '__main__':
    sol = Solution()
    xs = [2.00000, -2.0, 2.1, 2.0]
    ns = [-2147483648, 10, 3, -2]
    for x, n in zip(xs, ns):
        print(sol.myPow(x, n))