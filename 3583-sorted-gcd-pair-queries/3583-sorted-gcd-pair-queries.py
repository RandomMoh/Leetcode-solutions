from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        # Step 1: frequency count
        freq = [0] * (max_val + 1)
        for num in nums:
            freq[num] += 1
        
        # Step 2 & 3: Sieve + Möbius inversion
        # f[g] = number of pairs with GCD exactly g
        f = [0] * (max_val + 1)
        
        for g in range(max_val, 0, -1):
            # Count elements divisible by g
            cnt = sum(freq[g::g])           # harmonic series → O(max_val log max_val)
            pairs = cnt * (cnt - 1) // 2    # C(cnt, 2)
            # Subtract pairs with GCD = 2g, 3g, ...
            for multiple in range(2 * g, max_val + 1, g):
                pairs -= f[multiple]
            f[g] = pairs
        
        # Step 4: prefix sum for O(1) rank lookup
        prefix = []
        total = 0
        for g in range(1, max_val + 1):
            total += f[g]
            prefix.append(total)
        # prefix[i] = # pairs with GCD <= (i+1)
        
        # Answer each query with binary search
        return [bisect_right(prefix, q) + 1 for q in queries]