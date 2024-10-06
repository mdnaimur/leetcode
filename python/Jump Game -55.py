
class Solution:
    def canJamp(self, nums: list[int]) -> int:

        if not nums:
            return False

        maxrange = 0
        for i in range(len(nums)):
            if maxrange < i:
                return False
            maxrange = max(maxrange, i+nums[i])

        return maxrange >= len(nums)-1


nums = [7, 1, 5, 3, 6, 4]
# nums = [1, 2, 3, 4, 5]
# nums = [2, 3, 1, 1, 4]
# nums = [3, 2, 1, 0, 4]

sol = Solution()
result = sol.canJamp(nums)

print(result)
