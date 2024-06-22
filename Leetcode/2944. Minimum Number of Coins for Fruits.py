class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        prices = [0] + prices
        dp = [0 for _ in range(len(prices))]

        # 첫번째 과일 필수 구매
        dp[0] = 0
        dp[1] = prices[1]

        for i in range(2, len(dp)):
            res = float('inf')
            for j in range(ceil(i / 2), i):
                res = min(res, dp[j - 1] + prices[j])
            dp[i] = min(res, dp[i - 1] + prices[i])

        print(dp)
        return dp[len(prices) - 1]

