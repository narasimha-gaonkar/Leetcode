class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [-1] * (amount+1) 
        dp[0] = 0
        

        for i in range(1, amount+1):
            min_coins = float('inf')
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] != -1:
                     min_coins = min(min_coins, dp[i - coin] + 1)
                
            dp[i] = min_coins if min_coins != float('inf') else -1
                
        return dp[amount]
    
        #Recursive Approach
        '''
        dp = [-1] * (amount+1) 
        
        if amount == 0:
            return 0
        
        def solve(n):
            if n == 0:
                return 0
            
            if dp[n] != -1:
                return dp[n]
            
            min_s = float(inf)
            
            for coin in coins:
                
                if n - coin >= 0:
                    min_s = min(min_s, 1 + solve(n - coin))
            dp[n] = min_s
            return min_s
        solve(amount)

        return -1 if dp[amount] == float(inf) else dp[amount]
        
        '''
                