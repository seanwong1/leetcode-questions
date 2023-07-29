// Leetcode 3

var lengthOfLongestSubstring = function(s) {
  var storage = new Set();
  var beginning = 0;
  var largestString = 0;

  for (var end = 0; end < s.length; end++) {
    while (storage.has(s[end])) {
      storage.delete(s[beginning]);
      beginning++;
    }
    storage.add(s[end]);
    if (storage.size > largestString) {
      largestString = storage.size;
    }
  }
  return largestString;
}