
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        setNum = set()

        for num in nums:
            if nums in setNum:
                return True
            setNum.add(num)
        return False


# Time limit for complexity

# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:

#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#         return False
