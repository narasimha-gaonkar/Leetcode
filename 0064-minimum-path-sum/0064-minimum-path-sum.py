class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                    
                up = left = float(inf)
                
                if i > 0:
                    up = grid[i][j] + dp[i-1][j]
                if j > 0:
                    left = grid[i][j] + dp[i][j-1]
                dp[i][j] = min(up, left)
        
        return dp[m-1][n-1]
        
        
        @cache
        def solve(i, j):
            
            if i == 0 and j == 0:
                return grid[i][j]
            
            if i > 0:
                up = grid[i][j] + solve(i-1, j)
            else:
                up = float(inf)
            
            if j > 0:
                left = grid[i][j] + solve(i, j-1)
            else:
                left = float(inf)
            
            return min(up, left)
        
        return solve(m-1, n-1)
        