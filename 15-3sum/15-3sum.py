class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        
        nums.sort()
        
        idx , length = 0, len(nums)
        
        while idx<length:
            i, j = idx+1, length -1
            if idx ==0 or nums[idx] !=nums[idx-1]:
                while i<j:
                    summ = nums[idx]+ nums[i]+ nums[j]
                    if summ < 0:
                        i +=1
                    elif summ > 0:
                        j -=1
                    else:
                        result.add(tuple(sorted((nums[idx], nums[i], nums[j]))))
                        i+=1
                        j-=1
            idx+=1
            
        return result
        