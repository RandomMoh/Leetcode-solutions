from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        @lru_cache(None)
        def dp(i, m):
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            res = 0
            for x in range(1, 2 * m + 1):
                res = max(res, suffix_sum[i] - dp(i + x, max(m, x)))
            return res

        return dp(0, 1)