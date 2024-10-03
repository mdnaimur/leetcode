
class Solution:
    def canJamp(self, nums: list[int]) -> int:

        for i in range(1, len(nums)):
            if nums[i] >= nums[i-1]:
                return True
            else:
                return False


# nums = [7, 1, 5, 3, 6, 4]
# nums = [1, 2, 3, 4, 5]
# nums = [2, 3, 1, 1, 4]
nums = [3, 2, 1, 0, 4]

sol = Solution()
result = sol.canJamp(nums)

print(result)
