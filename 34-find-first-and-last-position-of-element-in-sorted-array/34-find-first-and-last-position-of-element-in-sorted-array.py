class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left_most_element = self.find_extremity(nums, target, "Left Extremity")
        right_most_element = self.find_extremity(nums, target, "Right Extremity")
        return [left_most_element, right_most_element]
        
    def find_extremity(self, nums, target, key):
        left_pointer, right_pointer, temp = 0, len(nums) - 1, -1
        while left_pointer <= right_pointer:
            middle = (left_pointer + right_pointer) // 2
            if nums[middle] < target: left_pointer = middle + 1
            elif target < nums[middle]: right_pointer = middle -1
            else:
                temp = middle
                if key == "Left Extremity": right_pointer = middle -1
                else: left_pointer = middle + 1
                    
        return temp