class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.prefix_sum = [0] * (len(nums)+1)
        for i in range(len(nums)):
            self.prefix_sum[i+1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

        '''
        very fast solution 

        def __init__(self, nums: List[int]):
        self.nums = nums

        def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])

        '''


nums = [-2, 0, 3, -5, 2, -1]

sol = NumArray(nums)
result = sol.sumRange(0, 5)

print(result)
