
# class Solution:
#     def maximumSwap(self, num: int) -> int:

#         maxValue = num
#         max_permutation_value = self.permutation(str(num))

#         if maxValue < max_permutation_value:
#             maxValue = max_permutation_value

#         return maxValue

#     def permutation(self, digits, current_digit=""):
#         if len(digits) == 0:
#             return int(current_digit)

#         max_permutation = int(current_digit) if current_digit else 0

#         for i in range(len(digits)):
#             new_permunation = current_digit + digits[i]
#             # print("new premunation", new_permunation)
#             remain_number = digits[:i]+digits[i+1:]
#             # print("remain mumber", remain_number)
#             perm_value = self.permutation(remain_number, new_permunation)
#             max_permutation = max(max_permutation, perm_value)

#         return max_permutation


# class Solution:
#     def maximumSwap(self, num: int) -> int:
#         # Convert the number to a list of digits.
#         num_str = list(str(num))

#         # Dictionary to record the last occurrence of each digit.
#         last_occurrences = {int(d): i for i, d in enumerate(num_str)}

#         # Traverse the list of digits.
#         for i, digit in enumerate(num_str):
#             # Check from 9 down to the current digit + 1.
#             for d in range(9, int(digit), -1):
#                 # If there's a larger digit later, swap and return.
#                 if last_occurrences.get(d, -1) > i:
#                     # Swap current digit with the larger digit.
#                     num_str[i], num_str[last_occurrences[d]
#                                         ] = num_str[last_occurrences[d]], num_str[i]
#                     # Convert the list back to integer and return.
#                     return int("".join(num_str))

#         # If no swap was done, return the original number.
#         return num


class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))

        max_digit = "0"
        max_i = -1
        swap_i = swap_j = -1

        for i in reversed(range(len(num))):

            # max
            if num[i] > max_digit:
                max_digit = num[i]
                max_i = i

            # swap
            elif num[i] < max_digit:
                swap_i, swap_j = i, max_i

            if swap_i != -1:
                # return int("".join(num))
                num[swap_i], num[swap_j] = num[swap_j], num[swap_i]

        return int("".join(num))


# num = 2736
num = 98368

sol = Solution()
result = sol.maximumSwap(num)

print(result)


# 100369. Count Substrings With K-Frequency Characters I

# 100421. Find the Sequence of Strings Appeared on the Screen
# 100453. Minimum Division Operations to Make Array Non Decreasing
#  100449. Check if DFS Strings Are Palindromes
