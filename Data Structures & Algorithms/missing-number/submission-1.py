class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        miss = 0
        while True:
            if not miss in nums:
                return miss
            miss += 1
