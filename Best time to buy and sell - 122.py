class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        maxProfit = 0

        for i in range(1, len(prices)):

            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
        return maxProfit


nums = [7, 1, 5, 3, 6, 4]
# nums = [1, 2, 3, 4, 5]

sol = Solution()
result = sol.maxProfit(nums)

print(result)
