def max_profit(prices):
    if len(prices) == 0:
        return 0
    
    buy = 0
    max_value = 0

    for sell in range(buy + 1, len(prices)):
        current_buy = prices[buy]

        total_profit = prices[sell] - current_buy

        if current_buy < prices[sell]:
            max_value = max(max_value, total_profit)
        else:
            buy = sell


    return max_value

prices = [7,1,5,3,6,4]
print(max_profit(prices))