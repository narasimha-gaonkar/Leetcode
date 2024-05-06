class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy1 = [float(-inf)] * n
        buy2 = [float(-inf)] * n
        
        buy1[0] = -prices[0]
        buy2[0] = -prices[0]
        sell1 = 0
        sell2 = 0
        
        for i in range(1, n):
            buy1[i] = max(buy1[i-1], - prices[i])
            sell1 = max(sell1, buy1[i] + prices[i])
            
            buy2[i] = max(buy2[i-1], sell1 - prices[i])
            sell2 = max(sell2, buy2[i] + prices[i])
        return sell2
            