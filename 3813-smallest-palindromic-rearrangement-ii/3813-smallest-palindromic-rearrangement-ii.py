import collections
import math

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        counts = collections.Counter(s)
        
        half_counts = {}
        mid = ""
        for char, count in counts.items():
            if count % 2 == 1:
                mid = char
            if count // 2 > 0:
                half_counts[char] = count // 2
                
        L = sum(half_counts.values())
        
        denom = 1
        for f in half_counts.values():
            denom *= math.factorial(f)
        P = math.factorial(L) // denom
        
        if P < k:
            return ""
            
        res_half = []
        chars = sorted(half_counts.keys())
        
        for _ in range(L):
            for c in chars:
                if half_counts[c] == 0:
                    continue
                
                cnt = (P * half_counts[c]) // L
                
                if cnt >= k:
                    res_half.append(c)
                    half_counts[c] -= 1
                    P = cnt
                    L -= 1
                    break
                else:
                    k -= cnt
                    
        left = "".join(res_half)
        return left + mid + left[::-1]