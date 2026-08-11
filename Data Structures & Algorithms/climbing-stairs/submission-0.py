class Solution:
    def helper(self, curr, n):
        if curr == n:
            self.count += 1
            return
        elif curr > n:
            return
        self.helper(curr+1, n)
        self.helper(curr+2, n)

    def climbStairs(self, n: int) -> int:
        self.count = 0
        self.helper(1, n)
        self.helper(2,n)
        return self.count