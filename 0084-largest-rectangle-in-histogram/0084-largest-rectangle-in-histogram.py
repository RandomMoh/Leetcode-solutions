class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights.append(0)
        stack = [-1]
        max_area = 0
        
        for i, h in enumerate(heights):
            while heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                if height * width > max_area:
                    max_area = height * width
            stack.append(i)
            
        return max_area