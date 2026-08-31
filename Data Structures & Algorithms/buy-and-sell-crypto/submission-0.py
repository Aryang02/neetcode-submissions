class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        l = 0
        r = l
        while r<len(prices):
            diff = prices[r] - prices[l]
            if diff < 0:
                l = r
            else:
                maxi = max(maxi, diff)
            r += 1
        return maxi