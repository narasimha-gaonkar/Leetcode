class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = amount + 1
        n = len(coins)
        dp = [[0] * n for _ in range(m)]
        
        for i in range(n):
            dp[0][i] = 1
        
        for i in range(1, m):
            for j in range(n):
                
                notpick = dp[i][j-1] if j >= 1 else 0
                pick = 0
                if i - coins[j] >= 0:
                    pick = dp[i - coins[j]][j] if i - coins[j] >= 0 else 0
                
                dp[i][j] = notpick + pick 
        # print(dp)       
        return dp[m-1][n-1]
        
        
        
#         @cache
#         def solve(amount, idx):
            
#             if amount == 0:
#                 return 1
#             if amount < 0:
#                 return 0
#             if idx < 0:
#                 return 0
            
#             pick = solve(amount - coins[idx], idx)
            
#             notpick = solve(amount, idx - 1)
            
#             return pick + notpick
        
#         return solve(amount, len(coins) - 1)