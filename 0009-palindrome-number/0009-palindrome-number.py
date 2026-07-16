class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending in 0 (except 0) are never palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # x == reversed_half        → even digits (e.g. 1221)
        # x == reversed_half // 10  → odd digits  (e.g. 121, middle digit ignored)
        return x == reversed_half or x == reversed_half // 10