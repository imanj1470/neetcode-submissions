class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        small = prices[0]
        for i in range(1, len(prices)):
            maxProfit = max(prices[i] - small, maxProfit)
            small = min(small, prices[i])

        return maxProfit
            
        