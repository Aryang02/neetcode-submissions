class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            print(i,n, diff)
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
