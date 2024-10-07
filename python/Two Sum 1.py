class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
           num_map = {}

        for i in range(len(nums)-1):
            sumValue = nums[i]+nums[i+1]

            if target == sumValue:
                result = {i,i+1}

        return result
        """
        # Dictionary to store previously visited numbers and their indices
        num_map = {}

        # Loop through the list to find the target pair
        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_map:
                return [num_map[complement], i]

            # Store the current number with its index in the dictionary
            num_map[num] = i

        # If no solution is found, return an empty list
        return []
