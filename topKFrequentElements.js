// Leetcod 347

var topKFrequent = function(nums, k) {
  var storage = new Array(nums.length + 1).fill().map(() => []);
  var counts = {};
  var mostFrequent = [];
  for (var i = 0; i < nums.length; i++) {
    if (!counts[nums[i]]) {
      counts[nums[i]] = 1;
    } else {
      counts[nums[i]]++;
    }
  }
  for (var key in counts) {
    storage[counts[key]].push(Number(key));
  }
  for (var i = storage.length - 1; i >= 0; i--) {
    for (var j = 0; j < storage[i].length; j++) {
      mostFrequent.push(storage[i][j]);
      if (mostFrequent.length === k) {
        return mostFrequent;
      }
    }
  }
};