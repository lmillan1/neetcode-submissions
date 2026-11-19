class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [3,4,5,6], target = 7
        # we need to find the complement, so we want to check if the
        # number exist in the set
        # if it does we want to return the indeces
        char_dict = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in char_dict:
                return [char_dict[complement], i]
            char_dict[num] = i
            
