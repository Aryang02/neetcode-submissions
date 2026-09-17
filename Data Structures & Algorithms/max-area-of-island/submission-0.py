class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        def dfs(i, j):
            if 0>i or i>=n or 0>j or j>=m or grid[i][j] == 0:
                return 0
            else:
                grid[i][j] = 0
                a = dfs(i+1, j)
                b = dfs(i-1, j)
                c = dfs(i, j+1)
                d = dfs(i, j-1)
                return 1 + a + b + c + d
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        
        return ans
