// Leetcode 191

var hammingWeight = function(n) {
  var nArray = n.toString(2).split('');
  var initValue = 0;
  return nArray.reduce(function(accumulator, currentValue) {return Number(accumulator) + Number(currentValue);});
};