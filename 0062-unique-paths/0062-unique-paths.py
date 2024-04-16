class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[-1] * n for _ in range(m)]
        
        def solve(i , j):
            
            if i == m - 1 and j == n-1:
                return 1
            
            if i >= m or j >= n:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            count = 0
            
            count = solve(i + 1, j) + solve(i, j + 1)
            
            dp[i][j] = count
            
            return count
                    
        return solve(0, 0)