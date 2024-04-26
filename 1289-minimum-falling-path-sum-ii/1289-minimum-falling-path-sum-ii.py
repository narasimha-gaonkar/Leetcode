class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
        
        m = len(grid)
        n = len(grid[0])
        
        dp = [[None] * n for _ in range(m)]
        
        for i in range(n):
            dp[0][i] = grid[0][i]
        
        for i in range(1, m):
            for j in range(n):
                option = float(inf)
                if j == 0:
                    option = min(dp[i-1][j+1:])
                elif j == n-1:
                    option = min(dp[i-1][:j])
                else:
                    option = min(min(dp[i-1][:j]), min(dp[i-1][j+1:]))
                    
                dp[i][j] = grid[i][j] + option
                
        return min(dp[m-1])
            
            