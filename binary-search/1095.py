# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """

class MountainArray:
    def __init__(self, arr) -> None:
        self.arr = arr
        self.cnt = 0

    def get(self, index: int) -> int:
        if self.cnt >= 100:
            raise NotImplementedError("Wrong Answer")
        self.cnt += 1
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # We hypothesize a direction arry denoting whether arr[i+1] > arr[i].
        # Here we use +1 denote >, and -1 denote <. The direction array 
        # is the same length as mountain_arr with specified -1 at the end, 
        # written as dir_arr=[+1, ..., -1].
        # Our goal is finding i such that dir_arr[:i] = +1, dir_arr[i:] = -1. 
        arr_len = mountain_arr.length()
        lo = 0 # arr[lo] < arr[lo + 1]
        hi = arr_len - 1 # arr[hi] > arr[hi + 1]
        while lo < hi:
            mid = lo + (hi - lo) // 2
            dir = mountain_arr.get(mid + 1) - mountain_arr.get(mid)
            if dir > 0:
                lo = mid + 1
            else:
                hi = mid
        mount = lo 

        # Left ascending array.
        lo = 0
        hi = mount + 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            val = mountain_arr.get(mid)
            if val < target:
                lo = mid + 1
            else:
                hi = mid
        left_idx = lo
        val = mountain_arr.get(left_idx)
        if val == target:
            return left_idx

        # Right descending array.
        lo = mount
        hi = arr_len - 1
        while lo < hi:
            mid = hi - (hi - lo) // 2
            val = mountain_arr.get(mid)
            if val >= target:
                lo = mid
            else:
                hi = mid - 1
        right_idx = lo
        val = mountain_arr.get(right_idx)
        if val == target:
            return right_idx
        
        return -1

if __name__ == '__main__':
    sol = Solution()
    arrs = [
        [1, 2, 3, 4, 5, 3, 1],
        [1, 2, 3, 4, 5, 3, 1],
        [0, 1, 2, 4, 2, 1],
        [0, 1, 2, 4, 2, 1]
    ]
    targets = [3, 4, 3, -1]
    for arr, target in zip(arrs, targets):
        mount_arr = MountainArray(arr)
        print(sol.findInMountainArray(target, mount_arr), mount_arr.cnt)