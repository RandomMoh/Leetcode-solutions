class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            # Early Exit: If the smallest number is > 0, we can never sum to 0
            if a > 0:
                break
                
            # Skip duplicate values for our first number 'a'
            if i > 0 and a == nums[i - 1]:
                continue
                
            # Use Two Pointers for the remaining array to find the other two numbers
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                three_sum = a + nums[l] + nums[r]
                
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    # Found a valid triplet
                    res.append([a, nums[l], nums[r]])
                    
                    # Move both pointers to look for other combinations
                    l += 1
                    r -= 1
                    
                    # Skip duplicate values for our 'left' pointer to avoid duplicate triplets
                    # (We don't need to do it for 'right' because moving 'left' past duplicates 
                    # will naturally force 'right' to adjust appropriately anyway)
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                        
        return res