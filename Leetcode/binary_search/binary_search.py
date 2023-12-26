from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        result = -1
        while start <= end:
            mid = int((start + end) / 2)
            if nums[mid] <= target:
                start = mid + 1
                result = mid
            else:
                end = mid - 1
        
        if nums[result] != target:
            return -1
        else:
            return result
