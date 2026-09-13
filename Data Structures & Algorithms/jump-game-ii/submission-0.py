class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        far = 0
        curr = 0
        for i in range(n-1):
            far = max(far, i+nums[i])
            if i == curr:
                jumps += 1
                curr = far
        
        return jumps
            