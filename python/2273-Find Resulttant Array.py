# class Solution:
#     def removeAnagrams(self, words: list[str]) -> list[str]:

#         if len(words) <= 1:
#             return words

#         word_count = {}

#         for i, word in enumerate(words):
#             count = [0] * 26

#             for j, eachWord in enumerate(word):
#                 count[ord(eachWord) - ord("a")] += 1

#             key = tuple(count)

#             if key not in word_count:
#                 word_count[key] = word

#         return list(word_count.values())


from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = [words[0]]  # Always keep the first word

        for i in range(1, len(words)):
            # Convert word to character frequency tuple
            if sorted(words[i]) != sorted(words[i - 1]):  # Compare with previous word
                result.append(words[i])

        return result


# num = ["abba", "baba", "bbaa", "cd", "cd"]
num = ["a", "b", "a"]
# num = ["a", "b", "c", "d", "e"]

sol = Solution()
result = sol.removeAnagrams(num)

print(result)
