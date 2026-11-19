class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we want to return a list 
        res = []
        nums.sort()

        # [-4, -1, -1, 0, 1, 2]
        for i, num in enumerate(nums):
            # stop early if the number is positive
            if num > 0:
                break
            # skip duplicate first number 
            if i > 0 and num == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1

            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum == 0:
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    left += 1
        return res

        print(nums)
        