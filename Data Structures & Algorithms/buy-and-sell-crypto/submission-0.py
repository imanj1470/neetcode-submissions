class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        big = 0
        small = 0
        for i, price in enumerate(prices):
            profit = max(prices[i:]) - price

            if profit > maxProfit:
                maxProfit = profit
        return maxProfit
            
        