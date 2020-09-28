class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        if n < 2:
            return 0
        
        cost = prices[0]
        profit = 0
        
        for i in range(1, n):
            if prices[i] < cost:
                cost = prices[i]
            
            if prices[i] > cost:
                profit = max(profit, prices[i] - cost)
        
        return profit
        