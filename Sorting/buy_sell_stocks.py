import sys
def maxProfit(A):
    min_stock = sys.maxsize
    profit = 0

    for stock in A:
        if(stock < min_stock):
            min_stock = stock
        elif(stock - min_stock > profit):
            profit = stock - min_stock
    return profit
            
A = [7,1,5,3,6,4]
print(maxProfit(A))
