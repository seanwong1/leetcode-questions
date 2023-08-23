// Leetcode 338

var hammingWeight = function(n) {
  var nArray = n.toString(2).split('');
  var initValue = 0;
  return nArray.reduce(function(accumulator, currentValue) {return Number(accumulator) + Number(currentValue);});
};

var countBits = function(n) {
  var numBits = [];
  for (var i = 0; i <= n; i++) {
    numBits.push(Number(hammingWeight(i)));
  }
  return numBits;
};