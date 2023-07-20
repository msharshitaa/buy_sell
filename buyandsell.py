def maxProfit(prices):
    profit = 0
    buy = prices[0]
    for sell in prices[1:]:
        if sell > buy:
            profit = max(profit, sell - buy)
        else:
            buy = sell
    return profit

prices=list(map(int,input().split()))
print(maxProfit(prices))