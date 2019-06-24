# If you were only permitted to complete at most one transaction
# (i.e., buy one and sell one share of the stock),
# Design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

import sys
def maxProfit(stocks):
    min_stock = sys.maxsize
    profit = 0

    for stock in stocks:
        if(stock < min_stock):
            min_stock = stock
        elif(stock - min_stock > profit):
            profit = stock - min_stock
    return profit

stocks = [7,1,5,3,6,4]
print(maxProfit(stocks))
