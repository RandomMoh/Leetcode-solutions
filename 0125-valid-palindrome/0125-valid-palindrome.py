class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move left pointer until it hits an alphanumeric char
            while left < right and not s[left].isalnum():
                left += 1
            
            # Move right pointer until it hits an alphanumeric char
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare the characters (lowercased)
            if s[left].lower() != s[right].lower():
                return False
            
            # Move both pointers inward
            left += 1
            right -= 1
            
        return True