class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        
        n = len(matrix[0])
        max_square = 0
        
        dp = [[0] * n for _ in range(m)]
        for i in range(n):
            dp[0][i] = int(matrix[0][i])
            
            max_square = max(max_square, dp[0][i])
        for j in range(m):
            dp[j][0] = int(matrix[j][0])
            
            max_square = max(max_square, dp[j][0] )
        for i in range(1, m):
            for j in range(1, n):
                
                if matrix[i][j] != '0':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_square =  max(max_square, dp[i][j])
        # print(dp)
        return max_square * max_square
                    
        
        
            
            
        