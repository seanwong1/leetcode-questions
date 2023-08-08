// Leetcode 125

var isPalindrome = function(s) {
  s = s.toLowerCase();
  var left = 0;
  var right = s.length - 1;
  while (left < right) {
    while ((left < right) && !isAlphaNum(s[left])) {
      left++;
    }
    while ((left < right) && !isAlphaNum(s[right])) {
      right--;
    }
    if (s[left] !== s[right]) {
      return false;
    }
  left++;
  right--;
  }
  return true;
};

var isAlphaNum = function(c) {
  return (c.charCodeAt(0) > 47 && c.charCodeAt(0) < 58) || (c.charCodeAt(0) > 96 && c.charCodeAt(0) < 123);
}