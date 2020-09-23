class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        last = -1
        result = 0

        for i in reversed(range(len(prices))):
            if last == -1:
                last = prices[i]
                continue
            if prices[i] <= last:
                result += last - prices[i]
            last = prices[i]

        return result
