class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [ 1, 2, 4, 6]
        # if we make two arrays of the size of nums and set to one 
        n = len(nums)

        left = [1] * n
        right = [1] * n

        print(left)
        print(right)

        for i in range(1, n): 
            left[i] = left[i - 1] * nums[i-1]
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        return [left[i] * right[i] for i in range(n)]