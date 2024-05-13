class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def solve(amount):
            
            if amount == 0:
                return 0
            
            if amount <= 0:
                return float(inf)
            
            
            steps = float(inf)
            for coin in coins:
                steps = min(steps, 1 + solve(amount - coin))
            
            return steps
        res = solve(amount)  
        return res if res != float(inf) else -1
                
                
            
        