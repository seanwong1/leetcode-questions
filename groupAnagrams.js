// Leetcode 49

var groupAnagrams = function(strs) {
  var groups = {};
  for (var i = 0; i < strs.length; i++) {
    var charCount = Array(26);
    charCount.fill(0);
    for (var j = 0; j < strs[i].length; j++) {
        charCount[strs[i].charCodeAt(j) - 97] += 1;
    }
    if (groups[charCount]) {
        groups[charCount].push(strs[i]);
    } else {
        groups[charCount] = [strs[i]];
    }
  }
  return Object.values(groups);
};