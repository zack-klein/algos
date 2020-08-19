def maxProfitBruteForce(prices):

    if prices == []:
        return 0

    profits = []

    for i, val in enumerate(prices):

        for j in range(i + 1, len(prices)):

            profit = prices[j] - val
            profits.append(profit)

    if profits == []:
        return 0

    elif max(profits) > 0:
        return max(profits)

    else:
        return 0


def maxProfitOnePass(prices):
    if prices == []:
        return 0

    min_price = max(prices)
    max_profit = 0

    for i, val in enumerate(prices):

        if val < min_price:
            min_price = val

        elif val - min_price > max_profit:
            max_profit = val - min_price

    return max_profit
