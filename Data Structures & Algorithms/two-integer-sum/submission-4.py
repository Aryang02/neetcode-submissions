class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        MAX = 10**9
        for i, num in enumerate(nums):
            if target - num in hmap:
                return [hmap[target- num], i]
            else:
                hmap[num] = min(hmap.get(num, MAX), i)