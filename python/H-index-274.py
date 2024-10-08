
class Solution:
    def hIndex(self, citations: list[int]) -> int:
        """
           [3,0,6,1,5]

            1-> 0
            2 -> 1
            3 -> 3
            4 -> 5
            5 -> 6 

            1-> 6
            2 -> 5
            3 -> 3
            4 -> 1
            5 -> 0

            index value compare the value if index value max to compare value then index value is reustl
        """

        citations.sort(reverse=True)

        for i in range(len(citations)):

            if i >= citations[i]:
                return i

        return len(citations)


nums = [7, 1, 5, 3, 6, 4]
# nums = [1, 2, 3, 4, 5]
# nums = [3, 0, 6, 1, 5]
# nums = [1, 3, 1]

sol = Solution()
result = sol.hIndex(nums)

print(result)
