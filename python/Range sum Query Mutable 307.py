class NumArray:

    def __init__(self, nums: list[int]):
        self.mynums = nums

    def update(self, index: int, val: int) -> None:
        self.mynums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.mynums[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
nums = [-2, 0, 3, -5, 2, -1]

sol = NumArray(nums)
result = sol.sumRange(0, 5)

print(result)
