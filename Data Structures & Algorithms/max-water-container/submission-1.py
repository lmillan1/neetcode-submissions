class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # return an int of the max amount of water  
        # were given a list of heights of type int
        max_area = 0
        left, right = 0 , len(heights) - 1 

        while left < right:
            cur_height = min(heights[left], heights[right])
            area = cur_height * (right-left)
            max_area = max(max_area, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
        