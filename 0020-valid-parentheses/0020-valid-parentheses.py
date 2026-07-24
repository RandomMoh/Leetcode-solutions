class Solution:
    def isValid(self, s: str) -> bool:
        # Quick exit for odd-length strings
        if len(s) % 2 != 0:
            return False
            
        stack = []
        match = {')': '(', '}': '{', ']': '['}
        
        for c in s:
            if c in match:
                # If stack is empty or top doesn't match the required open bracket
                if not stack or stack.pop() != match[c]:
                    return False
            else:
                stack.append(c)
                
        return not stack