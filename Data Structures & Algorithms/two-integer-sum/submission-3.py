class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map1 = {num:i for i, num in enumerate(nums)}
        
        for i, num in enumerate(nums):
            if target - num in map1 and map1[target-num] != i:
                return [i, map1[target-num]] 