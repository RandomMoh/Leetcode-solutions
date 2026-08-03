class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [0] * 4
        
        for i in range(n - 1, -1, -1):
            take = 0
            ans = float('-inf')
            for k in range(3):
                if i + k < n:
                    take += stoneValue[i + k]
                    ans = max(ans, take - dp[(i + k + 1) % 4])
            dp[i % 4] = ans
            
        res = dp[0]
        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        return "Tie"