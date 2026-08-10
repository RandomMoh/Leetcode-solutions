class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        squares = [i * i for i in range(1, int(n**0.5) + 1)]
        
        for i in range(1, n + 1):
            for s in squares:
                if s > i:
                    break
                if not dp[i - s]:
                    dp[i] = True
                    break
                    
        return dp[n]