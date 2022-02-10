class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = 0, len(nums) - 1
        lo = hi = -1
    
        while (lo == -1 or hi == -1) and len(nums) > 0:
            if nums[start] != target and lo == -1:
                start += 1
            if nums[end] != target and hi == -1:
                end -= 1

            if start > end:
                break

            if nums[start] == target:
                lo = start

            if nums[end] == target:
                hi = end
    
        return [lo, hi]