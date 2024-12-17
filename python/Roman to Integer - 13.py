class Solution:
    def romanToInt(self, s: str) -> int:

        RomanValue = {"I": 1, "V": 5, "X": 10,
                      "L": 50, "C": 100, "D": 500, "M": 1000}

        total = 0
        pre_value = 0

        for char in reversed(s):
            current_value = RomanValue[char]
            # print(current_value)

            if current_value < pre_value:
                total -= current_value
            else:
                total += current_value

            pre_value = current_value

        return total


# Example usage
solution = Solution()

# Test cases
print(solution.romanToInt("III"))  # Output: 3
print(solution.romanToInt("IV"))   # Output: 4
print(solution.romanToInt("IX"))   # Output: 9
print(solution.romanToInt("LVIII"))  # Output: 58
print(solution.romanToInt("MCMXCIV"))  # Output: 1994
