class Solution:
    # def lengthOfLastWord(self, s: str) -> int:

    #     word = s.strip().split()

    #     return len(word[-1]) if word else 0

    #  solution method 2

    def lengthOfLastWord(self, s: str) -> int:
        lenght = 0
        found_word = False

        for i in range(len(s)-1, -1, -1):

            if s[i] != ' ':
                lenght += 1
                found_word = True
            elif found_word:
                break
        return lenght


# Example usage
solution = Solution()

# Test cases
s1 = "Hello World"

print(solution.lengthOfLastWord(s1))
s = "   fly me   to   the moon  "
print(solution.lengthOfLastWord(s))
