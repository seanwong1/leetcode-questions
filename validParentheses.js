// Leetcode 20

var isValid = function(s) {
  sArray = s.split('');
  validParentheses = {')': '(', ']': '[', '}': '{'};
  var endBracket;
  var forwardBrackets = [];
  if (sArray.length % 2 === 1) {
    return false;
  }
  for (var i = 0; i < sArray.length; i++) {
    if (!validParentheses[sArray[i]]) {
      forwardBrackets.push(sArray[i]);
    } else {
      if (validParentheses[sArray[i]] !== forwardBrackets.pop()) {
        return false;
      }
    }
  }
  if (forwardBrackets.length > 0) {
    return false;
  }
  return true;
};