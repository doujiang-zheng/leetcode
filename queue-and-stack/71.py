from collections import deque

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        seq = path.split('/')
        for s in seq:
            if s == '':
                continue
            elif s == '.':
                continue
            elif s == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(s)
        
        ans = '/'.join(list(stack))
        return '/' + ans


if __name__ == '__main__':
    sol = Solution()
    paths = ["/home/", "/../", "/home//foo/", "/a/./b/../../c/"]
    for path in paths:
        print(sol.simplifyPath(path))