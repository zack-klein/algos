//
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
//


/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let minPrice = Infinity;
    let maxProfit = 0;

    for (var i = 0; i < prices.length; i++) {
        let price = prices[i];

        if (price < minPrice) {
            minPrice = price
        } else if (price - minPrice > maxProfit) {
            maxProfit = price - minPrice
        }
    };
    return maxProfit
};
