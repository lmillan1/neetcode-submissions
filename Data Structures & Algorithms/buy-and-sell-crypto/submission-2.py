class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # list of prices and we want to buy the max lowest and sell at the max possible days
        # return maximum profit of type int 
        max_profit = 0
        left, right = 0, 1 # left is our buy day and right is our sell

        for right in range(1, len(prices)):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
        return max_profit

        