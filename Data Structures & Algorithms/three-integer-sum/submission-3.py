class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            # Since nums is sorted, no three numbers starting > 0 can sum to 0
            if num > 0:
                break

            # Skip duplicate starting elements
            if i > 0 and num == nums[i - 1]:
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
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif three_sum > 0:
                    right -= 1
                else:
                    left += 1

        return res