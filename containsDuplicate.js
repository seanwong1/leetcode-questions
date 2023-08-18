// Leetcode 217

var containsDuplicate = function(nums) {
  var numsSet = new Set(nums);
  return numsSet.size !== nums.length;
};