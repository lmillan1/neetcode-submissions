class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]
        # left: [1, 1, 1, 1]
        # 
        # right:[1, 1, 1, 1]

        # [48, 24, 12, 8]

        n = len(nums)      
        prefix = [1] * n
        suffix = [1] * n

        # prefix 
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i +1]
        
        # multiply both

        return [prefix[i] * suffix[i] for i in range(n)]

        
        