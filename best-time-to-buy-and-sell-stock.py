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


# Revisiting this one after a long time!
def maxProfitBF(self, prices):
    max_profit = 0

    for i, buy in enumerate(prices):

        for sell in prices[i + 1 :]:  # noqa
            profit = sell - buy

            if profit > max_profit:
                max_profit = profit

    return max_profit


# This is ridiculously elegant (naturally had to look at the solution...)
def maxProfitOnePass2(self, prices):

    max_profit = 0
    min_price = float("inf")

    for price in prices:

        if price < min_price:
            min_price = price

        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit
