class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        dp = [[None] * n for _ in range(n)]
        
        for i in range(n):
            dp[0][i] = grid[0][i]
        
        for i in range(1, n):
            for j in range(n):
                option = float(inf)
                if j == 0:
                    option = min(dp[i-1][j+1:])
                elif j == n-1:
                    option = min(dp[i-1][:j])
                else:
                    option = min(min(dp[i-1][:j]), min(dp[i-1][j+1:]))
                    
                dp[i][j] = grid[i][j] + option
                
        return min(dp[n-1])
            
            