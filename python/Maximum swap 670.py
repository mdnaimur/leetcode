
class Solution:
    def maximumSwap(self, num: int) -> int:

        maxValue = num
        for i in range(1, 3):
            num /= 10
            print('num after division', num)
            temp = num % 10
            print('numer after modulation', temp)
            num = temp
            print('num after tem', num)
        if (maxValue < num):
            maxValue = num

        return maxValue


num = 2736

sol = Solution()
result = sol.maximumSwap(num)

print(result)


# 100369. Count Substrings With K-Frequency Characters I

# 100421. Find the Sequence of Strings Appeared on the Screen
# 100453. Minimum Division Operations to Make Array Non Decreasing
#  100449. Check if DFS Strings Are Palindromes
