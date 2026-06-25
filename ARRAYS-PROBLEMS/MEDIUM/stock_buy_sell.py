# Stock Buy and Sell
class Solution:
    def maxProfit(self, prices):
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    max_profit = max(max_profit, prices[j] - prices[i])

        return max_profit

if __name__ == "__main__":
    prices = list(map(int, input().split()))

    obj = Solution()
    print(obj.maxProfit(prices))


# Optimized Solution
class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

if __name__ == "__main__":
    prices = list(map(int, input().split()))

    obj = Solution()
    print(obj.maxProfit(prices))