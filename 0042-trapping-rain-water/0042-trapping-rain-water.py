class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = left_max if left_max > height[left] else height[left]
                water += left_max - height[left]
            else:
                right -= 1
                right_max = right_max if right_max > height[right] else height[right]
                water += right_max - height[right]
                
        return water