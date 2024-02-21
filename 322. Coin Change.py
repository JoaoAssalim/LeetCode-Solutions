class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount+1):
            for j in coins:
                if a - j >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-j])
        print(dp)
        return dp[amount] if dp[amount] != amount + 1 else -1
