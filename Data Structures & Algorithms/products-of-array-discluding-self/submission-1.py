class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [1] * n

        # prefix so any number before the current index
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # post fix so any number after the current index
        postfix = 1
        for i in range(n -1, -1,-1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
