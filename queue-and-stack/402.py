import collections


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # maintain a monotone non-decreasing stack, which
        # stores reserved digits.
        stack = collections.deque()
        cnt = 0
        for i, digit in enumerate(num):
            while stack and digit < stack[-1] and cnt < k:
                stack.pop()
                cnt += 1

            stack.append(digit)

        while stack and cnt < k:
            stack.pop()
            cnt += 1

        cnt_zero = 0
        for ch in stack:
            if ch == '0':
                cnt_zero += 1
            else:
                break

        if cnt_zero == len(stack):
            ans = '0'
        else:
            ans = ''.join(list(stack)[cnt_zero:])
        
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = ["1432219", "10200", "10"]
    ks = [3, 1, 2]
    for num, k in zip(nums, ks):
        print(sol.removeKdigits(num, k))