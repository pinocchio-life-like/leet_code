def buyChoco(self, prices, money):
    prices.sort()
    left = 0
    right = len(prices) - 1
    while left < right:
        total = prices[left] + prices[right]
        if total <= money:
            return money - total
        elif total > money:
            right -= 1
        else:
            left += 1
    return money