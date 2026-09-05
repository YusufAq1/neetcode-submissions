class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        if len(heights) == 2:
            return min(heights[0], heights[1])

        front = 0 
        back = len(heights)-1

        max = 0 
        while front < back:
            width = back - front
            min_height = min(heights[front], heights[back])
            stored_water = width * min_height 
            if stored_water > max:
                max = stored_water
            if heights[front] < heights[back]:
                front += 1
            elif heights[front] > heights[back]:
                back -= 1
            else:
                front += 1
                back -= 1

        return max
