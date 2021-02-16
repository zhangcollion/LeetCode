class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 0:
            return 0

        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        seen = []
        for i in range(1, n + 1):
            if i * i <= n:
                seen.append(i * i)
            else:
                break
        for i in range(1, n + 1):
            for square in seen:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[n]