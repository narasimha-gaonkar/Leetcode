class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[-1]* len(text2) for _ in range(len(text1))]
        
        def solve(n1, n2):
            if n1 < 0 or n2 < 0:
                return 0
            if dp[n1][n2] > -1:
                return dp[n1][n2]
            
            pick = 0
            notpick = 0
            if text1[n1] == text2[n2]:
                
                pick = 1 + solve(n1-1, n2-1)
            else:
                notpick = max(solve(n1-1, n2), solve(n1, n2-1))
           
            dp[n1][n2] = max(pick, notpick)
            return max(pick, notpick)
        
        return solve(len(text1) - 1, len(text2)-1)
            
        