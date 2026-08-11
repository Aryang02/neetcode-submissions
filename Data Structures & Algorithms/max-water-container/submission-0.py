class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        maxwater = 0
        while i<j:
            area = min(heights[i], heights[j])*(j-i)
            maxwater = max(maxwater, area)
            if heights[i]>heights[j]:
                j -= 1
            else:
                i += 1
        return maxwater