class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        min_price = float(inf)
        max_profit = 0
        for price in prices:
            if price > min_price:
                cur_profit = price - min_price
                
                max_profit += cur_profit
            min_price = price
        return max_profit
                
            
            