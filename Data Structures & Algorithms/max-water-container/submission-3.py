class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # formula to calculate the max amount of water
        # width = (right - left), height = min(heights[left], heights[right])
        left, right = 0, len(heights) - 1
        max_height = 0
        while left < right:
            current_height = (right - left) * (min(heights[left], heights[right]))
            max_height = max(max_height, current_height)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_height