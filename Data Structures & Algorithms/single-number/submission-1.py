class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        while len(nums) != 1:
            x = nums.pop()
            if x not in nums:
                return x
            else:
                nums.remove(x)
        return nums[0]

            