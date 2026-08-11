class Solution:
    def findMin(self, nums: List[int]) -> int:
        i , j = 0, len(nums) - 1 
        curr_min = float("inf")
        
        while i  <  j :
            mid = i + (j - i ) // 2
            curr_min = min(curr_min,nums[mid])
            
            if nums[mid] > nums[j]:
                i = mid + 1
                
            else:
                j = mid - 1 
                
        return min(curr_min,nums[i])
