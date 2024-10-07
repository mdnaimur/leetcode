
class Solution:
    def jump(self, nums: list[int]) -> int:

        n = len(nums)

        # if not nums:
        #     return len(nums)

        jumps = 0  # count the jums
        currentEnd = 0  # keep track of the farthest postion
        farthest = 0  # keep track fartest postion reach overall

        for i in range(n-1):
            farthest = max(farthest, i+nums[i])
            print(f"i is {i } and distance is {farthest}")

            if i == currentEnd:
                print("this is current end : ", currentEnd)
                jumps += 1
                currentEnd = farthest

        return jumps


# nums = [7, 1, 5, 3, 6, 4]
# nums = [1, 2, 3, 4, 5]
# nums = [2, 3, 1, 1, 4]
nums = [3, 2, 1, 0, 4]
nums1 = [2, 3, 1, 1, 4]

sol = Solution()
result = sol.jump(nums)

print(result)

result1 = sol.jump(nums1)

print(result1)
