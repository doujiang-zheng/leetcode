from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mmap = dict()
        for i, v in enumerate(nums):
            if v in mmap:
                mmap[v].add(i)
            else:
                mmap[v] = set([i])
        for i, v in enumerate(nums):
            other = target - v
            if other in mmap:
                if i in mmap[other] and len(mmap[other]) > 1:
                    s = mmap[other]
                    s.remove(i)
                    return [i, list(s)[0]]
                elif i not in mmap[other]:
                    s = list(mmap[other])[0]
                    return [i, s]
        return []


if __name__ == '__main__':
    sol = Solution()
    nums = [[2, 7, 11, 15], [3, 2, 4], [3, 3]]
    targets = [9, 6, 6]
    for num, target in zip(nums, targets):
        print(sol.twoSum(num, target))