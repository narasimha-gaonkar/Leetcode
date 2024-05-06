class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        
        min_buy = prices[0]
        
        for i in range(1, n):
            min_buy = min(min_buy, prices[i])
            
            dp[i] = max(dp[i-1], prices[i] - min_buy)
        
        return dp[n-1]
        
            
            