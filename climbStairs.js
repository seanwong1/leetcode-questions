// Leetcode 70

var climbStairs = function(n) {
  if (n === 1) {
    return 1;
  }
  var ratio = function(n) {
    const phi = (1 + Math.sqrt(5)) / 2;
    var sum = ((phi**n) - ((1 - phi)**n)) / (Math.sqrt(5));
    return sum;
  }
  return ratio(n) + ratio(n - 1);
};