class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] < 0:
                    continue
                cur_profit = prices[j] - prices[i]
                maxProfit = max(cur_profit, maxProfit)
        return maxProfit
        