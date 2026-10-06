class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy, sell = prices[0], prices[0]
        for idx in range(1, len(prices)):
            val = prices[idx]
            if val < buy:
                buy = val
                sell = val
                continue
            if val > sell and (val - buy) > profit:
                sell = val
                profit = sell - buy
        return profit