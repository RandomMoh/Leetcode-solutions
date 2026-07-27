class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        
        while l < r:
            m = (l + r) // 2
            if sum((p - 1) // m + 1 for p in piles) <= h:
                r = m
            else:
                l = m + 1
                
        return l