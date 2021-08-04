class Solution:
    def numberOfWeeks(self, milestones) -> int:
        if len(milestones) == 1:
            return 1
        max_num = max(milestones)
        tot = sum(milestones)
        if tot - max_num >= max_num:
            return tot
        else:
            return (tot - max_num) * 2 + 1

if __name__ == '__main__':
    examples = [[1, 2, 3], [5, 2, 1]]
    s = Solution()
    for example in examples:
        ans = s.numberOfWeeks(example)
        print(ans)