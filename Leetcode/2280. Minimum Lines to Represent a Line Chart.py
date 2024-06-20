class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        n = len(stockPrices)
        if n <= 2:
            return n-1
        stockPrices.sort(key = lambda x: x[0])
        days = [stockPrice[0] for stockPrice in stockPrices]
        prices = [stockPrice[1] for stockPrice in stockPrices]

        dx0 = days[1] - days[0]
        dy0 = prices[1] - prices[0]

        answer = 1
        for i in range(n-2):
            dy = prices[i+2] - prices[i+1]
            dx = days[i+2] - days[i+1]
            if dx * dy0 != dx0 * dy:
                dy0 = dy
                dx0 = dx
                answer += 1
        return answer