class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # The problem asks for 1-indexed results
                return [left + 1, right + 1]
                
            elif current_sum > target:
                # Sum is too large, make it smaller by moving the right pointer
                right -= 1
                
            else:
                # Sum is too small, make it larger by moving the left pointer
                left += 1