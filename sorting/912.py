import heapq
from typing import List
import random

class Solution:
    def partition(self, nums, low, high):
        # select the pivot randomly
        pi_idx = random.randint(low, high) 
        # swap pi_idx with high
        nums[pi_idx], nums[high] = nums[high], nums[pi_idx]
        pivot = nums[high]

        i = low - 1
        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        
        nums[i+1], nums[high] = nums[high], nums[i+1]
        return i + 1

    def quicksort(self, nums: List[int], low, high) -> None:
        if low >= high:
            return 

        pi = self.partition(nums, low, high)
        self.quicksort(nums, low, pi - 1)
        self.quicksort(nums, pi + 1, high) 
    
    def heapsort(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = heapq.heappop(nums)
        return ans

    def merge(self, nums: List[int], aux: List[int], low: int, mid: int, high: int) -> None:
        for i in range(low, high + 1):
            aux[i] = nums[i]
        
        p1 = low
        p2 = mid + 1
        for i in range(low, high + 1):
            if p1 > mid and p2 <= high:
                nums[i] = aux[p2]
                p2 += 1
            elif p1 <= mid and p2 > high:
                nums[i] = aux[p1]
                p1 +=1
            elif p1 <= mid and p2 <= high:
                if aux[p1] < aux[p2]:
                    nums[i] = aux[p1]
                    p1 +=1
                else:
                    nums[i] = aux[p2]
                    p2 +=1
            else:
                raise Exception("Two pointers p1 > mid and p2 > high.")

    def mergesort(self, nums: List[int], aux: List[int], low: int, high: int):
        if low < high:
            mid = low + (high - low) // 2
            self.mergesort(nums, aux, low, mid)
            self.mergesort(nums, aux, mid + 1, high)
            self.merge(nums, aux, low, mid, high)


    def sortArray(self, nums: List[int]) -> List[int]:
        # self.quicksort(nums, 0, len(nums) - 1)
        # nums = self.heapsort(nums)
        aux = [0] * len(nums)
        self.mergesort(nums, aux, 0, len(nums) - 1)
        return nums


if __name__ == '__main__':
    sol = Solution()
    nums = [[5, 2, 3, 1], [5, 1, 1, 2, 0, 0]]
    for num in nums:
        print(sol.sortArray(num))
