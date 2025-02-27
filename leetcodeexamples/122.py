# 122. Best Time to Buy and Sell Stock II

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        sell = prices[0]
        profit = 0
        total_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy or prices[i] < sell:
                buy = prices[i]
                sell = prices[i]
                total_profit += profit
                profit = 0
            elif prices[i] - buy > profit:
                sell = prices[i]
                profit = prices[i] - buy
            
        
        if buy != sell:
            total_profit += profit
        return total_profit