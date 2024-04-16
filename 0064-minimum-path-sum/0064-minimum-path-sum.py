class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        
        dp = [[-1] * n for _ in range(m)]
        
        def solve(i, j):
            
            if i == 0 and j == 0:
                return grid[i][j]
            
            if i < 0 or j < 0 or i > m or j > n:
                return float(inf)
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            up = grid[i][j] + solve(i-1, j) 
            left = grid[i][j] + solve(i, j - 1)
            
            dp[i][j] = min(up, left)
            
            return dp[i][j]
        
        return solve(m-1, n-1)

        
            
    
        