class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if len(nums)<2:
        #     return 0 if target in nums else -1
        # if len(nums) == 2:
        #     return index()
        # i, j = 0, len(nums)-1

        # while i<j:
        #     if nums[i] == target:
        #         return i
        #     if nums[j] == target:
        #         return j
        #     mid = (i+j)//2
        #     if nums[mid]>nums[j] and nums[mid]> target:
        #         i = mid+1
        #     elif nums[mid]<nums[j] and nums[mid]<target:
        #         j = mid-1
        #     elif nums[mid] == target:
        #         return mid
        # return -1
        try:
            return nums.index(target)
        except:
            return -1 
