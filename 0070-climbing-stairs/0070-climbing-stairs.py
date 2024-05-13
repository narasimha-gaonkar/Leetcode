class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [-1] * (n + 1)
        
        def solve(index):
            if index == 0:
                return 1
            
            if index < 0:
                return 0
            if dp[index] > 0:
                return dp[index]
            
            oneJump = solve(index - 1)
            
            twoJump = solve(index - 2)
            
            dp[index] = oneJump + twoJump
            
            return oneJump + twoJump
        
        return solve(n)