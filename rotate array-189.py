class Solution:

    def reverse(self, nums, i, j):
        li = i
        ri = j

        while (li < ri):
            temp = nums[li]
            nums[li] = nums[ri]
            nums[ri] = temp

            li += 1
            ri -= 1

    def rotate(self, nums: list[int], k):

        numLen = len(nums)

        k = k % numLen
        if k < 0:
            k += numLen

        self.reverse(nums, 0, numLen-k-1)
        self.reverse(nums, numLen-k, numLen-1)
        self.reverse(nums, 0, numLen-1)


nums = [-1, -100, 3, 99]
k = 2
sol = Solution()
sol.rotate(nums, k)
print(nums)
