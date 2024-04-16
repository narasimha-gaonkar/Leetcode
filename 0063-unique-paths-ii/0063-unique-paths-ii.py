class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1] * n for _ in range(m)]
        
        
        def solve(i, j):
            
            if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
                return 0
            if i == 0 and j == 0:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            
            count = solve(i-1, j) + solve(i, j-1)
            
            dp[i][j] = count
            
            return dp[i][j]
        
        return solve(m-1, n-1)
        
        
        
#         dp[0][0] = 1
        
#         for i in range(m):
#             for j in range(n):
#                 if i == 0 and j == 0:
#                     continue
                
#                 up, left = 0, 0
                
#                 if i > 0:
#                     up = dp[i-1][j]
                
#                 if j > 0:
#                     left = dp[i][j-1]
                
#                 dp[i][j] = up + left
                
#         return dp[m-1][n-1]