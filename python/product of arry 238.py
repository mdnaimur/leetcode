'''
array is = nums 
return ans = ans[i] = products of all elements of nums 
expect nunms[i]


'''


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        n = len(nums)
        ans = [1]*n
        products_pre = 1

        for num in range(n):
            ans[num] = products_pre
            products_pre = products_pre * nums[num]

        products_suf = 1

        for num in range(n-1, -1, -1):
            ans[num] *= products_suf
            products_suf = products_suf * nums[num]

        return ans
