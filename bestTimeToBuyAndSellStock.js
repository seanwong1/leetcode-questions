// Leetcode 121

var maxProfit = function(prices) {
  var result = 0;
  var buy = 0;
  var sell = buy + 1;
  while (sell < prices.length) {
    if (prices[sell] < prices[buy]) {
      buy = sell;
      sell = buy + 1;
    } else {
      if (prices[sell] - prices[buy] > result) {
        result = prices[sell] - prices[buy];
      } else {
        sell++;
      }
    }
  }
  return result;
};