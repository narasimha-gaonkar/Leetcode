class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[-1] * n for _ in range(m)]
        
        dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                up, left = 0, 0
                if i > 0:
                    up = dp[i-1][j]
                if j > 0:
                    left = dp[i][j-1]
                dp[i][j] = up + left
        return dp[m-1][n-1]