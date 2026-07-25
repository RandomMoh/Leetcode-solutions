class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            v = nums[m]
            
            if v == target:
                return m
            if v < target:
                l = m + 1
            else:
                r = m - 1
                
        return -1