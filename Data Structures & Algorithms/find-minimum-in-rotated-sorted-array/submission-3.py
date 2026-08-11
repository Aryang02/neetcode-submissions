class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        if nums[i] < nums[j]:
            return nums[i]
        minim = 10001
        while i<j:
            mid = (i+j)//2
            minim = min(minim, nums[mid])

            if nums[mid] > nums[j]:
                i = mid+1
            else:
                j = mid-1
        return min(minim, nums[i])