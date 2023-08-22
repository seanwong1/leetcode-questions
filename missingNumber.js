// Leetcode 268

var missingNumber = function(nums) {
  var supposedSum = nums.length * (nums.length + 1) / 2;
  for (var i = 0; i < nums.length; i++) {
    supposedSum -= nums[i];
  }
  return supposedSum;
};