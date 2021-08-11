# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
bad_version = 0
call_count = 0

def isBadVersion(version):
    global bad_version
    global call_count
    call_count += 1
    return version >= bad_version

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo = 1
        hi = n + 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if not isBadVersion(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo
        pass

if __name__ == '__main__':
    sol = Solution()
    versions = [5, 1]
    bads = [4, 1]
    for version, bad in zip(versions, bads):
        bad_version = bad
        call_count = 0
        print(sol.firstBadVersion(version), call_count) 