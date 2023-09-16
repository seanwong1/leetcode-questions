var getDigit = function(num, place) {
  return Math.floor(Math.abs(num) / (10 ** place) % 10);
}

var digitCount = function(num) {
  if (!num) {
    return 1;
  }
  return Math.floor(Math.log10(Math.abs(num))) + 1
}

var mostDigits = function(nums) {
  var maxDigits = 0;
  for (var i = 0; i < nums.length; i++) {
    maxDigits = Math.max(maxDigits, digitCount(nums[i]));
  }
  return maxDigits;
}

var radixSort = function(nums) {
  const maxDigitCount = mostDigits(nums);
  for (var k = 0; k < maxDigitCount; k++) {
    var buckets = Array(10).fill(0).map(() => []);
    for (var i = 0; i < nums.length; i++) {
      buckets[getDigit(nums[i], k)].push(nums[i]);
    }
    nums = [].concat(...buckets);
  }
  return nums;
}