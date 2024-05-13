class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def solve(amount, idx):
            
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            if idx < 0:
                return 0
            
            pick = solve(amount - coins[idx], idx)
            
            notpick = solve(amount, idx - 1)
            
            return pick + notpick
        
        return solve(amount, len(coins) - 1)