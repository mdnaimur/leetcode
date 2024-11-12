
class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)

        if n == 0:
            return 0

        candies = [1]*n

        for i in range(1, n):
            print('inside loop', ratings[i])
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
                print("candies ", candies[i])

        for i in range(n - 2, -1, -1):
            print('2ndinside loop', ratings[i])
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


# nums = [3, 2, 1, 0, 4]
nums = [1, 0, 2]


sol = Solution()
result = sol.candy(nums)

print(result)

# nums1 = [2, 3, 1, 1, 4]
# result1 = sol.jump(nums1)

# print(result1)
