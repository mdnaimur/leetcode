class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:

        def has_unique_digits(num):
            print(f"[DEBUG] 1:  {(set(str(num)))}\n")
            print(f"[DEBUG] 2:  { str(num)}")
            print(len(set(str(num))) == len(str(num)))
            print("____________________________________________________")
            return len(set(str(num))) == len(str(num))

        result = 0
        limit = 10 ** n

        for i in range(limit):
            if has_unique_digits(i):
                result += 1

        return result


# Optimal Solution

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        calculation, result, temp = 9, 10, 9

        for i in range(1, n):
            calculation *= temp
            result += calculation
            temp -= 1
        return result


num = 8
# num = ["a", "b", "c", "d", "e"]

sol = Solution()
result = sol.countNumbersWithUniqueDigits(num)

print(result)
