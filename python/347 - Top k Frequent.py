class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        '''
         nums = [1,1,1,2,2,3]
         1's = 3 times 
         2's = 2 times
         3's = 1 time 
         k = 2
         top k elemets need print 
        '''

        numsDic = {}
        result = []
        counter = 0

        for i, num in enumerate(nums):

            if num in numsDic:
                numsDic[num] += 1
            else:
                numsDic[num] = 1

        for i, value in enumerate(numsDic):
            result.append(value)
            counter += 1
            if counter == k:
                break
        return result


nums = [3, 0, 1, 0]
k = 1

sol = Solution()
result = sol.topKFrequent(nums, k)

print(result)
