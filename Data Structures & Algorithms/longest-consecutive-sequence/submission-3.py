class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(sorted(set(nums)))
        print(nums)
        max_len = 1
        cur_len = 1
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] != 1:
                max_len = max(max_len, cur_len)
                cur_len = 0
            cur_len += 1
        max_len = max(max_len, cur_len)
        return max_len 