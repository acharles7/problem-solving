"""
If you were only permitted to complete at most one transaction 
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""


def max_profit(prices: List[int]) -> int:
    if not prices: return 0

    cur_minimum = prices[0]
    max_profit  = 0

    for price in prices:
        max_profit  = max(max_profit, price-cur_minimum)
        cur_minimum = min(cur_minimum, price)
    return max_profit

