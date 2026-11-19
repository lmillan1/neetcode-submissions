class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # optimal
        dict_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in dict_map:
                return [dict_map[complement], i]
            dict_map[num] = i


        # Brute Force 0(N^2)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []
