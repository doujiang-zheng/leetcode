class Solution:
    primes = []

    def find_prime(self, n=100):
        primes = self.primes
        primes.append(2)
        for i in range(3, n + 5, 2):
            flag = True
            for p in primes:
                if i % p == 0:
                    flag = False
                    break
            if flag:
                primes.append(i)


    def isThree(self, n: int) -> bool:
        primes = self.primes
        if len(primes) == 0:
            self.find_prime()
        
        flag = False
        for p in primes:
            if p * p > n:
                break
            if p * p == n:
                flag = True
        return flag

if __name__ == '__main__':
    arr = [2, 4]
    s = Solution()
    for i in arr:
        ans = s.isThree(i)
        print(ans)