class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1 , 2 , 3 , 4 target = 3
        # |           |
        # numbers[l] + numbers[r] == target 
        # if number

        left, right = 0 , len(numbers) - 1 

        while left < right:
            curSum = numbers[left] + numbers[right]

            if curSum > target:
                right -= 1
            elif curSum < target:
                left += 1
            else:
                return [left + 1, right + 1 ]
        return []