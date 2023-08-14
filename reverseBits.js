// Leetcode 190

var reverseBits = function(n) {
  var nArray = n.toString(2).split('').reverse();
  while (nArray.length < 32) {
    nArray.push('0')
  }
  return parseInt(nArray.join(""), 2);
};