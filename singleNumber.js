// Leetcode 136

var singleNumber = function(nums) {
  var numOccurence = {};
  for (var i = 0; i < nums.length; i++) {
    if (!numOccurence[nums[i]]) {
      numOccurence[nums[i]] = 1;
    } else {
      delete numOccurence[nums[i]];
    }
  }
  return Number(Object.keys(numOccurence)[0]);
};