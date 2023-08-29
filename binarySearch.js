// Leetcode 704

var search = function(nums, target, index = 0) {
  var midpoint = Math.floor(nums.length / 2);
  var left = nums.slice(0, midpoint);
  var right = nums.slice(midpoint, nums.length);
  if (target > nums[nums.length - 1] || target < nums[0]) {
    return -1;
  } else if (nums[midpoint] === target) {
    return index + midpoint;
  } else if (target > nums[midpoint]) {
    return search(right, target, index + midpoint);
  } else if (target < nums[midpoint]) {
    return search(left, target, index);
  }
};