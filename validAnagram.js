// Leetcode 242

var isAnagram = function(s, t) {
  var sArray = s.split('').sort();
  var tArray = t.split('').sort();
  if (sArray.length !== tArray.length) {
    return false;
  }
  for (var i = 0; i < sArray.length; i++) {
    if (sArray[i] !== tArray[i]) {
      return false;
    }
  }
  return true;
};