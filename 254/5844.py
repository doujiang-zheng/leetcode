class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        mod = int(1e9 + 7)
        # if p == 1:
        #     return 1
        # if p == 2:
        #     return 6
        # if p == 3:
        #     return 1512
        # 1 ... 2^p-2 2^p-1
        # minimum: (2^p-1) * (2^p-2)^(2^{p-1}-1) mod 10e9+7
        # => (2^p-1) mod 10e9+7 * (2^p-2)^r mod 10e9+7
        #    where 2^{p-1} - 1 = k * \phi(10e9+7) + r
        two_power_p = 1
        for i in range(1, p + 1):
            two_power_p = (two_power_p * 2) % mod

        phi_prime = mod - 1
        power_res = 1
        for i in range(1, p):
            power_res = (power_res * 2) % phi_prime # \phi(10e9+7) = 10e9+6
        # assume power_res >= 0, r = (2^{p-1} - 1) % \phi(10e9+7)
        power_res = (power_res - 1 + phi_prime) % phi_prime
        
        # solve: (2^p-2)^r mod (10e9+7)
        term2 = 1
        base_power = two_power_p - 2
        while power_res > 0:
            if power_res & 1:
                term2 = (term2 * base_power) % mod
            base_power = (base_power * base_power) % mod
            power_res >>= 1
        
        # solve: (2^p - 1) mod (10e9+7)
        term1 = (two_power_p - 1) % mod
        ans = (term1 * term2 + mod) % mod
        return ans


if __name__ == '__main__':
    sol = Solution()
    ps = [1, 2, 3]
    for p in ps:
        print(sol.minNonZeroProduct(p))