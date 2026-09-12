max_profit = 0 #brute force
for i in range(0,len(prices)):
    for j in range(i+1,len(prices)):
        profit = prices[j] - prices[i]
        if profit >= max_profit:
                    max_profit = profit

#return max_profit

#optimal solution
min_price = prices[0]
max_profit = 0
for i in range(0,len(prices)):
    if prices[i] <= min_price:
                min_price = prices[i]
    else:
                new_profit = prices[i] - min_price
                max_profit = max(max_profit,new_profit)

#return max_profit