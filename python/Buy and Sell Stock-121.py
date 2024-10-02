class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        maxProfit = 0

        for price in prices:

            if price < min_price:
                min_price = price
                print("min price update:", min_price)
            currentProfit = price - min_price

            if (currentProfit > maxProfit):
                maxProfit = currentProfit
        return maxProfit


nums = [7, 1, 5, 3, 6, 4]

sol = Solution()
result = sol.maxProfit(nums)

print(result)
