// Leetcode 66

var plusOne = function(digits, digit = digits.length - 1) {
  if (digits[digit] === 9) {
    digits[digit] = 0;
    if (digit - 1 < 0) {
      digits.unshift(1);
    }
    return plusOne(digits, digit - 1);
  } else {
    digits[digit] += 1;
  }
  return digits;
};